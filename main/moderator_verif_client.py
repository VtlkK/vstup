from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Clients, Sing_Clients,Moderator, verificate_photo_client, verif, Anketa, documents, corup, zgoda_bat
from django.shortcuts import render, redirect, get_object_or_404
def aut3(request, id):
    moder_id = request.session.get('id')
    moder = get_object_or_404(Moderator, id=moder_id)
    el = get_object_or_404(Clients, id=id)
    img34 = verificate_photo_client.objects.filter(client_id=el.id)

    if request.method == 'POST':
        try:

            Sing_Clients.objects.filter(client_id=el.id).delete()
            Anketa.objects.filter(client_id=el.id).delete()
            verificate_photo_client.objects.filter(client_id=el.id).delete()
            documents.objects.filter(client_id=el.id).delete()
            corup.objects.filter(client_id=el.id).delete()
            zgoda_bat.objects.filter(client_id=el.id).delete()
            Clients.objects.filter(id=el.id).delete()
            return redirect('moderator', moder.id)
        except Exception as e:
            print(f'Error: {e}')

    return render(request, 'main/mod_verific.html', {'img34': img34, 'el': el})

def ver(request, id):
    moder_id = request.session.get('id')
    moder = get_object_or_404(Moderator, id=moder_id)
    el = get_object_or_404(Clients, id=id)
    if request.method == 'POST':
        verify = request.POST.get('verify', None)
        if verify:
            objv = verif(
                client=el,
                verify_client=verify
            )
            objv.save()

        return redirect('moderator', moder.id)
    return render(request, 'main/mod_verific.html', {'el': el})