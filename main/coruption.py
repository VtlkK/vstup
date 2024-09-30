from django.http import HttpResponseForbidden

from .models import Clients, corup
from django.shortcuts import render, redirect, get_object_or_404

def corupt(request, id):
    el = Clients.objects.get(id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    if corup.objects.filter(client_id=el.id).exists():
       return redirect('cabinet', id=el.id)
    if request.method == 'POST':
        f22 = request.POST['f22']
        obj123 = corup(
            client=el,
            f22=f22
        )
        obj123.save()
        return redirect('cabinet', id=el.id)
    return render(request, 'main/corruption.html')