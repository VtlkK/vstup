from django.shortcuts import get_object_or_404, render, redirect
from main.models import Clients, vlk_napr, Moderator
from django.views.decorators.cache import never_cache

@never_cache
def vlkN(request, id):
    moder_id = request.session.get('id')
    moder = get_object_or_404(Moderator, id=moder_id)
    el = Clients.objects.get(id=id)
    if request.method == 'POST':
        pdf = request.FILES['pdf']
        obj = vlk_napr(client=el, pdf=pdf)
        obj.save()
        return redirect('moderator', moder.id)
    return render(request, 'main/naprav.html', {'client': el})