from django.http import HttpResponseForbidden

from .models import Clients, Med
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache

@never_cache
def edit_med(request, id):
    el = get_object_or_404(Clients, id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    obj33 = get_object_or_404(Med, client_id=el.id)
    if request.method == 'POST':
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

        obj33.pos_v = pos_v
        obj33.psix = psix
        obj33.protu_tub = protu_tub
        obj33.antutila = antutila
        obj33.skira = skira
        obj33.f025 = f025
        obj33.f027 = f027
        obj33.f063 = f063
        obj33.an_s = an_s
        obj33.bio_h = bio_h
        obj33.ser_an_k = ser_an_k
        obj33.ant_b = ant_b
        obj33.ant_c = ant_c
        obj33.rw = rw
        obj33.flu = flu
        obj33.ekg = ekg
        obj33.an_kr =an_kr

        obj33.save()
        return redirect('cabinet', id=id)
    else:
        edit = {
            'psix': obj33.psix,
            'ekg': obj33.ekg,
            'flu': obj33.flu,
            'rw': obj33.rw,
            'ant_c': obj33.ant_c,
            'ant_b': obj33.ant_b,
            'ser_an_k': obj33.ser_an_k,
            'bio_h': obj33.bio_h,
            'an_s': obj33.an_s,
            'f063': obj33.f063,
            'f027': obj33.f027,
            'f025': obj33.f025,
            'skira': obj33.skira,
            'antutila': obj33.antutila,
            'pos_v': obj33.pos_v,
            'protu_tub': obj33.protu_tub,
            'an_kr': obj33.an_kr
        }
    return render(request, 'main/edit_med.html', {'edit': edit})