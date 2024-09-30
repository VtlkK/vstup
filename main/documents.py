from django.http import HttpResponseForbidden

from .models import Clients, documents
from django.shortcuts import render, redirect, get_object_or_404

def document(request, id):
    el = Clients.objects.get(id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    if documents.objects.filter(client_id=el.id).exists():
        return redirect('cabinet', id=el.id)
    if request.method == 'POST':
        id_card = request.FILES['id_card']
        id_card2 = request.FILES['id_card2']
        location_doc = request.FILES['location_doc']
        born_doc = request.FILES['born_doc']
        plat_doc = request.FILES['plat_doc']
        spec_doc = request.FILES['spec_doc']
        photo_doc = request.FILES['photo_doc']
        cruminal_doc = request.FILES['cruminal_doc']
        psix_doc = request.FILES['psix_doc']
        obj9 = documents(
                client=el,
                id_card=id_card,
                id_card2=id_card2,
                location_doc=location_doc,
                born_doc=born_doc,
                plat_doc=plat_doc,
                spec_doc=spec_doc,
                photo_doc=photo_doc,
                cruminal_doc=cruminal_doc,
                psix_doc=psix_doc
            )
        obj9.save()
        return redirect('cabinet', el.id)
    return render(request, 'main/document.html', {'el': el})