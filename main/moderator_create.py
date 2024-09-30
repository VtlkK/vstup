from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Moderator


def ModeratorCreate(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        hashed_password = make_password(password)

        obj = Moderator(login=login, password=hashed_password)
        obj.save()
        request.session['id'] = obj.id
        return redirect('moderator_login')
    return render(request, 'main/moderator_create.html')


def moderator_login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        try:
            moder = Moderator.objects.get(login=login)
            if check_password(password, moder.password):
                moder.save()
                request.session['id'] = moder.id
                idd = request.session.get('id')
                if idd is None or int(idd) != int(moder.id):
                    return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
                return redirect('moderator', moder.id)
            else:
                return render(request, 'main/modertor_login.html', {'error': 'Неправильний логін або пароль'})
        except Moderator.DoesNotExist:
            return render(request, 'main/modertor_login.html', {'error': 'Неправильний логін або пароль'})

    return render(request, 'main/modertor_login.html')


def logout_view(request):
    logout(request)
    return redirect('moderator_login')
