from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from .models import Clients,zgoda_bat
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

@never_cache
def zgoda_ofor(request, id):
    el = Clients.objects.get(id=id)
    idd = request.session.get('id')
    error_list = []

    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")

    if zgoda_bat.objects.filter(client_id=el.id).exists():
        return redirect('cabinet', id=el.id)

    if request.method == 'POST':
        photo_zgodu = request.FILES.get('photo_zgodu')

        if not photo_zgodu:
            error_list.append("Будь ласка, завантажте файл.")
        elif photo_zgodu.content_type not in ['image/jpeg', 'image/png', 'image/gif']:
            error_list.append("Будь ласка, завантажте тільки зображення (JPEG, PNG, GIF).")
        else:
            obj12 = zgoda_bat(client=el, photo_zgodu=photo_zgodu)
            obj12.save()
            return redirect('cabinet', id=el.id)


    return render(request, 'main/parents_consent.html', {'error_list': error_list, 'client': el})