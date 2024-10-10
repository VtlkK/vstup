from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Clients, Sing_Clients, verif
import json
import re

from django.views.decorators.cache import never_cache
from dotenv import load_dotenv

load_dotenv()



def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('------------------------')
    print(f"IP адреса клієнта: {ip}")
    print('------------------------')
    return render(request, 'main/index.html')



@never_cache
@csrf_exempt
def CreatUser(request):
    if request.method == 'POST':
        name = request.POST['name']
        soname = request.POST['soname']
        fname = request.POST['fname']
        name2 = request.POST['name2']
        soname2 = request.POST['soname2']
        fname2 = request.POST['fname2']
        date = request.POST['date']
        email = request.POST['email']
        military = request.POST['military']
        born = request.POST['born']
        document = request.POST['document']
        num = request.POST['num']
        login = request.POST['login']
        password = request.POST['password']
        lang = request.POST['lang']
        pogad = request.POST['pogad']
        sex = request.POST['sex']
        place_med = request.POST['place_med']

        if Clients.objects.filter(login=login).exists():
            return render(request, 'main/signup.html', {'error': 'Такий логін вже існує'})
        if len(password) < 8:
            return render(request, 'main/signup.html', {'error': 'Пароль має містити не менше 8 символів.'})

        if not re.search(r'[a-z]', password):
            return render(request, 'main/signup.html', {'error': 'Пароль має містити принаймні одну малу літеру.'})

        if not re.search(r'[A-Z]', password):
            return render(request, 'main/signup.html', {'error': 'Пароль має містити принаймні одну велику літеру.'})

        if not re.search(r'[\W_]', password):
            return render(request, 'main/signup.html',
                          {'error': 'Пароль має містити принаймні один спеціальний символ.'})

        hashed_password = make_password(password)

        obj = Clients(login=login, password=hashed_password)
        obj.save()
        request.session['id'] = obj.id
        request.session.save()

        obj1 = Sing_Clients(client=obj, pogad=pogad, place_med=place_med, sex=sex, name=name, soname=soname, fname=fname, name2=name2, soname2=soname2, fname2=fname2, date=date,
                            born=born, document=document, num=num, lang=lang, military=military, email=email)

        obj1.save()

        return redirect(reverse('cabinet', kwargs={'id': obj.id}))
    else:

        return render(request, 'main/signup.html')

def page_not_found(request):
    return HttpResponse('404 Не найдено', status=404)



def json_request(id):
    try:
        el = verif.objects.get(id=id)
        v = el.verify_client
        return JsonResponse({'v': v})
    except verif.DoesNotExist:
        return JsonResponse({'error': 'Дані для користувача не знайдено', 'v': None}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)