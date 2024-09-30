from django.http import HttpResponseForbidden

from .models import Clients, corup
from django.shortcuts import render, redirect, get_object_or_404
def edit_cor(request, id):
    el = get_object_or_404(Clients, id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    obj123 = get_object_or_404(corup, client_id=el.id)

    if request.method == 'POST':
        f22 = request.POST['f22']
        obj123.f22 = f22
        obj123.save()
        return redirect('cabinet', id=id)
    else:
        edit = {
            'f22': obj123.f22
        }
    return render(request, 'main/edit_coruption.html', {'edit': edit})