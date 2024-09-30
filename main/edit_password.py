import secrets

from django.core.mail import send_mail
import string
import random
from .models import Clients, re_password
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import timedelta
def restore_password(request, length=7):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            re_password.objects.filter(email=email).delete()

            characters = string.ascii_letters + string.digits
            reset_code = ''.join(secrets.choice(characters) for _ in range(length))

            obj = re_password(email=email, code=reset_code)
            obj.save()

            send_mail(
                'Відновлення пароля',
                f'Код для відновлення пароля: {reset_code}',
                'vstup_nadpsu@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('password2')

    return render(request, 'main/password.html')


def restore_password2(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        code1 = request.POST.get('code')

        try:
            email_obj = re_password.objects.get(email=email1)

            if timezone.now() - email_obj.created_at > timedelta(minutes=30):
                email_error = "Термін дії коду відновлення закінчився"
                return render(request, 'main/password2.html', {'email_error': email_error})

            if email_obj.code != code1:
                code_error = "Не вірний код"
                return render(request, 'main/password2.html', {'code_error': code_error})

            return redirect('edit_password')
        except re_password.DoesNotExist:
            email_error = "Не вірний email"
            return render(request, 'main/password2.html', {'email_error': email_error})

    return render(request, 'main/password2.html')


def edit_password(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        hash_password = make_password(password)

        try:
            client_obj = Clients.objects.get(login=login)
            client_obj.password = hash_password
            client_obj.save()
            return redirect('login')
        except Clients.DoesNotExist:
            login_error = "Такого логіна не існує"
            return render(request, 'main/password_edit.html', {'login_error': login_error})
        except Exception as e:
            error_message = f"Помилка: {str(e)}"
            return render(request, 'main/password_edit.html', {'error_message': error_message})

    return render(request, 'main/password_edit.html')