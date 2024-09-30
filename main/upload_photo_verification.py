from django.http import HttpResponseForbidden

from main.forms import verifyForm
from .models import Clients, verificate_photo_client
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

@never_cache
def verify2(request, id):
    el = Clients.objects.get(id=id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    if verificate_photo_client.objects.filter(client_id=el.id).exists():
        return redirect('cabinet', id=id)
    if request.method == 'POST':
        form = verifyForm(request.POST, request.FILES)
        if form.is_valid():
            verify_instance = form.save(commit=False)
            verify_instance.client = el
            verify_instance.save()
            return redirect('cabinet', id=el.id)
    else:
        form = verifyForm()

    return render(request, 'main/upload_photo_for_verification.html', {'form': form})