from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from main.models import napravlen, Clients, Moder_napr

from django.views.decorators.cache import never_cache

@never_cache
def otr_napr(request, id):
    try:
        el = Clients.objects.get(id=id)
    except Clients.DoesNotExist:
        return HttpResponseNotFound("Користувач не знайдений.")
    if request.method == "POST":
        true_false = request.POST.get("true_false")
        obj = napravlen(
            client=el,
            true_false=true_false
        )
        obj.save()
        return redirect('cabinet', el.id)




def moder_napr_otr(request, id):
    client = Clients.objects.get(id=id)
    napr = Moder_napr.objects.filter(client=client)

    return render(request, 'main/moder_napr_otr.html', {'napr': napr})