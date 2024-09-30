from django.http import HttpResponseForbidden

from .models import Clients, Med
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache

@never_cache
def med_docs(request, id):
    el = get_object_or_404(Clients, id=id)
    m = Med.objects.get(client_id=el.id)
    return render(request, 'main/med_docs.html', {'m': m})