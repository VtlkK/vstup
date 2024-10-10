from django.shortcuts import get_object_or_404

from .models import *
from django.http import JsonResponse

def json_request_ver(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
        verif_id = verif.objects.get(client_id=el.id)

        if verif_id.verify_client == 'verify':
            return JsonResponse({'v': 'verified'})
        else:
            return JsonResponse({'v': 'pending'})
    except verif.DoesNotExist:
        return JsonResponse({'v': 'not_found'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def json_request_tf(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
        tf_id = Mod_TF.objects.get(client_id=el.id)

        if tf_id.tf1 == True:
            return JsonResponse({'tf1': 'True'})
        else:
            return JsonResponse({'tf1': 'False'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def json_request_tf5(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
        tf5_id = Mod_TF.objects.get(client_id=el.id)

        if tf5_id.tf5 == True:
            return JsonResponse({'tf5': 'True'})
        else:
            return JsonResponse({'tf5': 'False'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def json_request_tf4(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
        tf4_id = Mod_TF.objects.get(client_id=el.id)

        if tf4_id.tf4 == True:
            return JsonResponse({'tf4': 'True'})
        else:
            return JsonResponse({'tf4': 'False'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def json_request_tf7(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
        tf7_id = Mod_TF.objects.get(client_id=el.id)

        if tf7_id.tf7 == True:
            return JsonResponse({'tf7': 'True'})
        else:
            return JsonResponse({'tf7': 'False'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def json_request_tf6(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
        tf6_id = Mod_TF.objects.get(client_id=el.id)

        if tf6_id.tf6 == True:
            return JsonResponse({'tf6': 'True'})
        else:
            return JsonResponse({'tf6': 'False'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def json_vlk(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
        napr_id = vlk_napr.objects.filter(client_id=el.id).first()

        if napr_id and napr_id.client_id == el.id:
            return JsonResponse({'napr': 'True'})
        else:
            return JsonResponse({'napr': 'False'})
    except vlk_napr.DoesNotExist:
        return JsonResponse({'napr': 'not_found'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

