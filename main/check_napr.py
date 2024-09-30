from django.shortcuts import redirect, get_object_or_404

from .models import check_napr, Clients, Moderator


def check_napravlen(request,id):
    el = Clients.objects.get(id=id)
    moder_id = request.session.get('id')
    moder = get_object_or_404(Moderator, id=moder_id)
    if request.method == 'POST':
        check2 = request.POST['check2']

        obj = check_napr(check2=check2, client=el)
        obj.save()
        return redirect('moderator', moder.id)
