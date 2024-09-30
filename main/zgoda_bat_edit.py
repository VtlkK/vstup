from django.http import HttpResponseForbidden

from .models import Clients,zgoda_bat
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache

@never_cache
def edit_zgoda(request, id):
    el = get_object_or_404(Clients, id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    obj12 = get_object_or_404(zgoda_bat, client_id=el.id)
    if request.method == 'POST':
        photo_zgodu = request.FILES['photo_zgodu']
        obj12.photo_zgodu = photo_zgodu

        obj12.save()
        return redirect('cabinet', id=el.id)
    else:
            initial_data = {
                'photo_zgodu': obj12.photo_zgodu,
            }
    return render(request,'main/edit_zgoda.html', {'intitial_data': initial_data})