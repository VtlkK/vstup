from django.http import HttpResponseForbidden

from .models import Clients,zgoda_bat
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

@never_cache
def zgoda_ofor(request, id):
    el = Clients.objects.get(id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    if zgoda_bat.objects.filter(client_id=el.id).exists():
        return redirect('cabinet', id=el.id)  #
    if request.method == 'POST':
        photo_zgodu = request.FILES['photo_zgodu']


        obj12 = zgoda_bat(
            client=el,
            photo_zgodu=photo_zgodu,
        )
        obj12.save()
        return redirect('cabinet', id=el.id)

    return render(request, 'main/parents_consent.html')