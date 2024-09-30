from django.http import HttpResponseForbidden

from .models import Clients, Med
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache

@never_cache
def med(request, id):
    el = get_object_or_404(Clients, id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    if Med.objects.filter(client_id=el.id).exists():
        return redirect('cabinet', id=el.id)
    if request.method == "POST":
        pos_v = request.POST.get('pos_v', '❌')
        psix = request.POST.get('psix', '❌')
        protu_tub = request.POST.get('protu_tub', '❌')
        antutila = request.POST.get('antutila', '❌')
        skira = request.POST.get('skira', '❌')
        f025 = request.POST.get('f025', '❌')
        f027 = request.POST.get('f027', '❌')
        f063 = request.POST.get('f063', '❌')

        an_kr = request.POST.get('an_kr', '❌')
        an_s = request.POST.get('an_s', '❌')
        bio_h = request.POST.get('bio_h', '❌')
        ser_an_k = request.POST.get('ser_an_k', '❌')
        ant_b = request.POST.get('ant_b', '❌')
        ant_c = request.POST.get('ant_c', '❌')
        rw = request.POST.get('rw', '❌')
        flu = request.POST.get('flu', '❌')
        ekg = request.POST.get('ekg', '❌')

        obj33 = Med(
            client=el,
            pos_v=pos_v, psix=psix, protu_tub=protu_tub, antutila=antutila,
            skira=skira, f025=f025, f027=f027, f063=f063, an_kr=an_kr, an_s=an_s,
            bio_h=bio_h, ser_an_k=ser_an_k, ant_b=ant_b, ant_c=ant_c, rw=rw, flu=flu,
            ekg=ekg
        )
        obj33.save()
        return redirect('cabinet', id=el.id)
    return render(request, 'main/med.html')