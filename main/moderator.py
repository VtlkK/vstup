from audioop import reverse

from django.http import HttpResponseForbidden, HttpResponseNotFound

from .models import (Clients, Anketa, Sing_Clients, Mod_TF,
                     Filter, vid_red, nadatu_dozvil,
                     Med, zgoda_bat, corup, documents, check_napr, Moderator,Moder_napr
                    )
from django.shortcuts import render, redirect, get_object_or_404
import psycopg2

from django.db.models import Q
from dotenv import load_dotenv
import os
load_dotenv()

def moderator(request, id):

    moders = Moderator.objects.all()
    moder = Moderator.objects.get(id=id)
    moderators = request.session.get('id')

    filter = Filter(request.GET, queryset=Sing_Clients.objects.all())
    filter_count = filter.qs.count()
    end = Clients.objects.filter(check_napr2__isnull=False).distinct()
    end_count = Clients.objects.filter(check_napr2__isnull=False).distinct().count()
    filtered_ver = Clients.objects.filter(verify2__isnull=False).distinct()
    clients_with_tf1 = Clients.objects.filter(mod_tf__tf1=True).distinct()
    filtered_ank = Clients.objects.filter(Anketa__isnull=False).distinct().exclude(id__in=clients_with_tf1.values_list('id', flat=True)).distinct()
    clients_with_all_tf = Clients.objects.filter(mod_tf__tf5=True, mod_tf__tf4=True, mod_tf__tf7=True).distinct()
    filtered_doc = Clients.objects.filter(documents__isnull=False).distinct().exclude(
        id__in=clients_with_all_tf.values_list('id', flat=True))
    filtered_cor = Clients.objects.filter(corup__isnull=False).distinct().exclude(
        id__in=clients_with_all_tf.values_list('id', flat=True))
    filtered_zg = Clients.objects.filter(zgoda__isnull=False).distinct().exclude(
        id__in=clients_with_all_tf.values_list('id', flat=True))
    clients_with_tf6 = Clients.objects.filter(mod_tf__tf6=True).distinct()
    filtered_med = Clients.objects.filter(Med__isnull=False).distinct().exclude(id__in=clients_with_tf6.values_list('id', flat=True)).distinct()

    combined_filtered = filtered_cor & filtered_zg & filtered_doc
    clients_with_vlk_n = Clients.objects.filter(vlk__isnull=False).distinct().exclude()
    filtered_nap = Clients.objects.filter(napravl__isnull=False).exclude(
        id__in=clients_with_vlk_n.values_list('id', flat=True)).distinct()
    users_with_vid_red = Clients.objects.filter(
        Q(vid_red2__anketa_red__isnull=False) |
        Q(vid_red2__corup_red__isnull=False) |
        Q(vid_red2__med_red__isnull=False) |
        Q(vid_red2__documents_red__isnull=False) |
        Q(vid_red2__zgoda_bat_red__isnull=False)
    ).distinct()
    filter_vid_nap = Clients.objects.filter(moder_napr__isnull=False).distinct()
    filtered_vid_nap_count = Clients.objects.filter(moder_napr__isnull=False).distinct().count()
    filtered_ver_count = Clients.objects.filter(verify2__isnull=False).exclude(verif__isnull=False).count()
    filtered_ank_count = Clients.objects.filter(Anketa__isnull=False).distinct().exclude(
        id__in=clients_with_tf1.values_list('id', flat=True)).distinct().count()
    filtered_med_count = Clients.objects.filter(Med__isnull=False).distinct().exclude(
        id__in=clients_with_tf6.values_list('id', flat=True)).distinct().count()
    combined_filtered_count = combined_filtered.count()

    filtered_nap_count = Clients.objects.filter(napravl__isnull=False).exclude(
        id__in=clients_with_vlk_n.values_list('id', flat=True)).distinct().count()

    clients_with_changes = set()
    clients_with_tfe = set()
    clients = Clients.objects.all()
    ell = Sing_Clients.objects.all()
    Anketa_img = Anketa.objects.all()
    count_hidden = 0

    clients_data_dict = {}
    for client in clients:

        try:
            tf = Mod_TF.objects.get(client_id=client.id)
        except Mod_TF.DoesNotExist:
            tf = None

        dozvil = nadatu_dozvil.objects.filter(client=client).first()
        vid_red2 = vid_red.objects.filter(client=client).first()

        hide_client = False

        if dozvil and vid_red2:
            if (dozvil.anketa_dozvil == vid_red2.anketa_red and
                    dozvil.corup_dozvil == vid_red2.corup_red and
                    dozvil.med_dozvil == vid_red2.med_red and
                    dozvil.documents_dozvil == vid_red2.documents_red and
                    dozvil.zgoda_dozvil == vid_red2.zgoda_bat_red):
                hide_client = True
                count_hidden += 1

        try:
            anketa = Anketa.objects.get(client_id=client.id)
        except Anketa.DoesNotExist:
            anketa = None
        try:
            coruption = corup.objects.get(client_id=client.id)
        except corup.DoesNotExist:
            coruption = None
        try:
            docs = documents.objects.get(client_id=client.id)
        except documents.DoesNotExist:
            docs = None
        try:
            zgoda = zgoda_bat.objects.get(client_id=client.id)
        except zgoda_bat.DoesNotExist:
            zgoda = None
        try:
            med_doc = Med.objects.get(client_id=client.id)
        except Med.DoesNotExist:
            med_doc = None

        anketa_last_modified = anketa.last_modified if anketa else None
        anketa_created = anketa.created if anketa else None
        coruption_last_modified = coruption.last_modified if coruption else None
        coruption_created = coruption.created if coruption else None
        docs_last_modified = docs.last_modified if docs else None
        docs_created = docs.created if docs else None
        zgoda_last_modified = zgoda.last_modified if zgoda else None
        zgoda_created = zgoda.created if zgoda else None
        med_doc_last_modified = med_doc.last_modified if med_doc else None
        med_doc_created = med_doc.created if med_doc else None

        changes_made = {
            'documents': docs_last_modified and docs_created and docs_last_modified > docs_created,
            'corup': coruption_last_modified and coruption_created and coruption_last_modified > coruption_created,
            'zgoda': zgoda_last_modified and zgoda_created and zgoda_last_modified > zgoda_created,
            'anketa': anketa_last_modified and anketa_created and anketa_last_modified > anketa_created,
            'med': med_doc_last_modified and med_doc_created and med_doc_last_modified > med_doc_created,
        }
        if any(changes_made.values()):
            clients_with_changes.add(client.id)

        combined_tfe = {
            'documents': Clients.objects.filter(documents__isnull=False).distinct().exclude(
                id__in=Clients.objects.filter(mod_tf__tfe5=True).values_list('id', flat=True)),
            'corup': Clients.objects.filter(corup__isnull=False).distinct().exclude(
                id__in=Clients.objects.filter(mod_tf__tfe3=True).values_list('id', flat=True)),
            'zgoda': Clients.objects.filter(zgoda__isnull=False).distinct().exclude(
                id__in=Clients.objects.filter(mod_tf__tfe2=True).values_list('id', flat=True)),
            'anketa': Clients.objects.filter(Anketa__isnull=False).distinct().exclude(
                id__in=Clients.objects.filter(mod_tf__tfe1=True).values_list('id', flat=True)),
            'med': Clients.objects.filter(Med__isnull=False).distinct().exclude(
                id__in=Clients.objects.filter(mod_tf__tfe4=True).values_list('id', flat=True)),
        }
        if any(client.id in combined_tfe[key].values_list('id', flat=True) for key in combined_tfe):
            clients_with_tfe.add(client.id)

        moder = Moderator.objects.get(id=id)
        idd = request.session.get('id')

        if idd is None or int(idd) != int(moder.id):
            return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")

        client_data = {
            'client': client,
            'tf': tf,
            'dozvil': dozvil,
            'hide_client': hide_client,
            'changes_made': changes_made,
            'show_in_list': any(
                changes_made[key] and client.id in combined_tfe[key].values_list('id', flat=True)
                for key in changes_made
            ),

        }
        clients_data_dict[client.id] = client_data
    total_users = users_with_vid_red.count()
    final_user_count = total_users - count_hidden
    final_count = len(clients_with_tfe)
    return render(request, 'main/moderator.html', {
        'filter': filter,
        'clients_data_dict': clients_data_dict,
        'clients': clients,
        'Anketa_img': Anketa_img,
        'filter_ver': filtered_ver,
        'filtered_ank': filtered_ank,
        'filtered_med': filtered_med,
        'combined_filtered': combined_filtered,
        'filtered_nap': filtered_nap,
        'ell': ell,
        'users_with_vid_red': users_with_vid_red,
        'moders': moders,
        'moderators': moderators,
        'moder': moder,
        'filtered_ver_count': filtered_ver_count,
        'filtered_ank_count': filtered_ank_count,
        'filtered_med_count': filtered_med_count,
        'combined_filtered_count': combined_filtered_count,
        'filtered_nap_count': filtered_nap_count,
        'filter_count': filter_count,
        'filtered_vid_nap_count': filtered_vid_nap_count,
        'filter_vid_nap': filter_vid_nap,
        'final_user_count': final_user_count,
        'final_count': final_count,
        'end_count': end_count,
        'end': end,

    })


def items(request, id):
    el = get_object_or_404(Clients, id=id)
    moder_id = request.session.get('id')
    moder = get_object_or_404(Moderator, id=moder_id)
    try:
        m = Med.objects.get(client_id=el.id)
    except Med.DoesNotExist:
        m = None

    if m is not None:
        date3 = m.last_modified > m.created
    else:
        date3 = False

    try:
        a = Anketa.objects.get(client_id=el.id)
    except Anketa.DoesNotExist:
        a = None

    if a is not None:
        date1 = a.last_modified > a.created
    else:
        date1 = False

    try:
        z = zgoda_bat.objects.get(client_id=el.id)
    except zgoda_bat.DoesNotExist:
        z = None

    if z is not None:
        date2 = z.last_modified > z.created
    else:
        date2 = False

    try:
        c = corup.objects.get(client_id=el.id)
    except corup.DoesNotExist:
        c = None

    if c is not None:
        date4 = c.last_modified > c.created
    else:
        date4 = False

    try:
        d = documents.objects.get(client_id=id)
    except documents.DoesNotExist:
        d = None

    if d is not None:
        date5 = d.last_modified > d.created
    else:
        date5 = False

    try:
        ank = Anketa.objects.get(client_id=el.id)
    except Anketa.DoesNotExist:
        ank = None

    try:
        zgo = zgoda_bat.objects.get(client_id=el.id)
    except zgoda_bat.DoesNotExist:
        zgo = None

    try:
        el2 = Sing_Clients.objects.get(client_id=el.id)
    except Sing_Clients.DoesNotExist:
        el2 = None

    try:
        docum = documents.objects.get(client_id=el.id)
    except documents.DoesNotExist:
        docum = None
    try:
        dozvil = nadatu_dozvil.objects.get(client_id=el.id)
    except nadatu_dozvil.DoesNotExist:
        dozvil = None

    conn = psycopg2.connect(
        dbname=os.environ.get("DATABASE_NAME"),
        user=os.environ.get("DATABASE_USER"),
        password=os.environ.get("DATABASE_PASSWORD"),
        host='localhost',
        port='5432',
    )

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM main_sing_clients WHERE client_id=%s", (el.id,))
    za = cur.fetchone()[0] > 0

    cur.execute("SELECT COUNT(*) FROM main_anketa WHERE client_id=%s", (el.id,))
    an = cur.fetchone()[0] > 0

    cur.execute("SELECT COUNT(*) FROM main_corup WHERE client_id=%s", (el.id,))
    coruptions = cur.fetchone()[0] > 0

    cur.execute("SELECT COUNT(*) FROM main_zgoda_bat WHERE client_id=%s", (el.id,))
    zgoda2 = cur.fetchone()[0] > 0

    cur.execute("SELECT COUNT(*) FROM main_documents WHERE client_id=%s", (el.id,))
    docs = cur.fetchone()[0] > 0

    cur.execute("SELECT COUNT(*) FROM main_mod_tf WHERE client_id=%s", (el.id,))
    tf = cur.fetchone()[0] > 0

    cur.execute("SELECT COUNT(*) FROM main_med WHERE client_id=%s", (el.id,))
    meds = cur.fetchone()[0] > 0

    cur.close()
    conn.close()
    try:
        tf = Mod_TF.objects.get(client_id=el.id)
    except Mod_TF.DoesNotExist:
        tf = None

    try:
        vv = vid_red.objects.get(client_id=el.id)
    except vid_red.DoesNotExist:
        vv = None
    try:
        doz = nadatu_dozvil.objects.get(client_id=el.id)
    except nadatu_dozvil.DoesNotExist:
        doz = None

    if request.method == 'POST':
            tf1 = request.POST.get('tf1')
            tf2 = request.POST.get('tf2')
            tf3 = request.POST.get('tf3')
            tf4 = request.POST.get('tf4')
            tf5 = request.POST.get('tf5')
            tf6 = request.POST.get('tf6')
            tf7 = request.POST.get('tf7')
            tfe1 = request.POST.get('tfe1', None)
            tfe2 = request.POST.get('tfe2', None)
            tfe3 = request.POST.get('tfe3', None)
            tfe4 = request.POST.get('tfe4', None)
            tfe5 = request.POST.get('tfe5', None)

            if tf:

                if tf1:
                    tf.tf1 = tf1
                if tf2:
                    tf.tf2 = tf2
                if tf3:
                    tf.tf3 = tf3
                if tf4:
                    tf.tf4 = tf4
                if tf5:
                    tf.tf5 = tf5
                if tf6:
                    tf.tf6 = tf6
                if tf7:
                    tf.tf7 = tf7
                if tfe1:
                    tf.tfe1 = tfe1
                if tfe2:
                    tf.tfe2 = tfe2
                if tfe3:
                    tf.tfe3 = tfe3
                if tfe4:
                    tf.tfe4 = tfe4
                if tfe5:
                    tf.tfe5 = tfe5
            else:
                tf = Mod_TF(
                    client=el,
                    tf1=tf1, tf2=tf2, tf3=tf3,
                    tf4=tf4, tf5=tf5, tf6=tf6,
                    tf7=tf7, tfe1=tfe1, tfe2=tfe2,
                    tfe3=tfe3, tfe4=tfe4, tfe5=tfe5
                )
            tf.save()
            return redirect('items', el.id)

    return render(request, 'main/info2.html', {
        'ank': ank,
        'zgo': zgo,
        'za': za,
        'an': an,
        'el2': el2,
        'docs': docs,
        'docum': docum,
        'coruptions': coruptions,
        'zgoda2': zgoda2,
        'el': el,
        'tf': tf,
        'meds': meds,
        'dozvil': dozvil,
        'date1': date1,
        'date2': date2,
        'date3': date3,
        'date4': date4,
        'date5': date5,
        'm': m,
        'doz': doz,
        'vv': vv,
        'moder': moder
    })


def save_dozvil_data(request, id):
    el = get_object_or_404(Clients, id=id)
    try:
        doz = nadatu_dozvil.objects.get(client_id=el.id)
    except nadatu_dozvil.DoesNotExist:
        doz = None
    if request.method == "POST":
        anketa_dozvil = request.POST.get('anketa_dozvil')
        corup_dozvil = request.POST.get('corup_dozvil')
        zgoda_dozvil = request.POST.get('zgoda_dozvil')
        documents_dozvil = request.POST.get('documents_dozvil')
        med_dozvil = request.POST.get('med_dozvil')

        if doz:
            doz.anketa_dozvil = anketa_dozvil or doz.anketa_dozvil
            doz.corup_dozvil = corup_dozvil or doz.corup_dozvil
            doz.zgoda_dozvil = zgoda_dozvil or doz.zgoda_dozvil
            doz.documents_dozvil = documents_dozvil or doz.documents_dozvil
            doz.med_dozvil = med_dozvil or doz.med_dozvil
        else:
            doz = nadatu_dozvil(
                client=el,
                anketa_dozvil=anketa_dozvil, corup_dozvil=corup_dozvil,
                zgoda_dozvil=zgoda_dozvil, documents_dozvil=documents_dozvil,
                med_dozvil=med_dozvil
            )
        doz.save()
        return redirect('items', el.id)




