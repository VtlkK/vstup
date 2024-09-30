from django.http import HttpResponseForbidden

from .models import Clients, documents
from django.shortcuts import render, redirect, get_object_or_404
def edit_document(request, id):
    el = get_object_or_404(Clients, id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    obj9 = get_object_or_404(documents, client_id=el.id)
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

        obj9.id_card = id_card
        obj9.id_card2 = id_card2
        obj9.location_doc = location_doc
        obj9.born_doc = born_doc
        obj9.plat_doc = plat_doc
        obj9.spec_doc = spec_doc
        obj9.photo_doc = photo_doc

        obj9.cruminal_doc = cruminal_doc
        obj9.psix_doc = psix_doc
        obj9.save()
        return redirect('cabinet', id=el.id)
    else:
        edit = {
            'id_card': obj9.id_card,
            'id_card2': obj9.id_card2,
            'location_doc': obj9.location_doc,
            'born_doc': obj9.born_doc,
            'plat_doc': obj9.plat_doc,
            'spec_doc': obj9.spec_doc,
            'photo_doc': obj9.photo_doc,

            'cruminal_doc': obj9.cruminal_doc,
            'psix_doc': obj9.psix_doc
        }
    return render(request, 'main/edit_docs.html', {'edit': edit})