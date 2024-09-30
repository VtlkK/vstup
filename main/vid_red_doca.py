from django.http import HttpResponseNotFound
from django.shortcuts import redirect

from main.models import vid_red, Clients
from django.views.decorators.cache import never_cache

@never_cache
def red_zaput(request, id):
    try:
        el = Clients.objects.get(id=id)
    except Clients.DoesNotExist:
        return HttpResponseNotFound("Користувач не знайдений.")
    try:
        red = vid_red.objects.get(client_id=el.id)
    except vid_red.DoesNotExist:
        red = None
    if request.method == "POST":
        anketa_red = request.POST.get('anketa_red', None)
        corup_red = request.POST.get('corup_red', None)
        zgoda_bat_red = request.POST.get('zgoda_bat_red', None)
        documents_red = request.POST.get('documents_red', None)
        med_red = request.POST.get('med_red', None)
        if red:
            if anketa_red:
                red.anketa_red = anketa_red
            if corup_red:
                red.corup_red = corup_red
            if zgoda_bat_red:
                red.zgoda_bat_red = zgoda_bat_red
            if documents_red:
                red.documents_red = documents_red
            if med_red:
                red.med_red = med_red
        else:
            red = vid_red(
                client=el,
                anketa_red=anketa_red,
                corup_red=corup_red,
                zgoda_bat_red=zgoda_bat_red,
                documents_red=documents_red,
                med_red=med_red
            )
        red.save()
        return redirect('cabinet', el.id)