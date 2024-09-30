from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import Clients
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from django_ratelimit.decorators import ratelimit

from django.views.decorators.cache import never_cache
#Вхід
@never_cache
@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def login(request):
    if request.method == 'POST':
        login_name = request.POST.get('login')
        password = request.POST.get('password')
        try:
            user = Clients.objects.get(login=login_name)
            if check_password(password, user.password):
                user.last_login = timezone.now()
                user.save()
                request.session['id'] = user.id
                idd = request.session.get('id')
                if idd is None or int(idd) != int(user.id):
                    return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
                return redirect(reverse('cabinet', kwargs={'id': user.id}))
            else:
                return render(request, 'main/login.html', {'error': 'Неправильний логін або пароль'})
        except Clients.DoesNotExist:
            return render(request, 'main/login.html', {'error': 'Неправильний логін або пароль'})

    return render(request, 'main/login.html')

def Unset_User(request):
    request.session.flush()
    return True

#Вихід з акаунта
def logout_view(request):
    logout(request)
    Unset_User(request)
    return redirect('home')