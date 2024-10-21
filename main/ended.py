from django.shortcuts import get_object_or_404, redirect

from .models import *


def ended(request, id):
    el = get_object_or_404(Clients, id=id)
    anketa = Anketa.objects.filter(client_id=el.id).first()

    if request.method == 'POST':
        ended = request.POST.get('ended')

        if anketa:
            anketa.ended = ended
            anketa.save()
        else:
            anketa = Anketa(client=el, ended=ended)
            anketa.save()

        return redirect('edit_anketa', el.id)



