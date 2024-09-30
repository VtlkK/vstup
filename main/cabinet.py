import psycopg2
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest
from .models import (Clients, Sing_Clients, nadatu_dozvil, vid_red,
                      Mod_TF, napravlen, zgoda_bat, documents, corup,
                      Anketa, Med, verif, vlk_napr, Moder_napr)
from django.shortcuts import render, redirect, get_object_or_404
from dotenv import load_dotenv
import os

load_dotenv()

def Cabinet(request, id):
    try:
        el = get_object_or_404(Clients, id=id)
    except Clients.DoesNotExist:
        return HttpResponseNotFound("Користувач не знайдений.")
    idd = request.session.get('id')
    print(f"{idd} 'idd")
    user = Clients.objects.get(id=idd)
    print(f"Request user ID: {user.id}, URL ID: {id}")

    if user.id != int(id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")

    el2 = Sing_Clients.objects.get(client_id=el.id)
    try:
        dozvil = nadatu_dozvil.objects.get(client_id=el.id)
    except nadatu_dozvil.DoesNotExist:
        dozvil = None
    try:
        vid_napr = Moder_napr.objects.filter(client_id=el.id)
    except Moder_napr.DoesNotExist:
        vid_napr = None
    try:
        red = vid_red.objects.get(client_id=el.id)
    except vid_red.DoesNotExist:
        red = None
    try:
        vlk_n = napravlen.objects.filter(client_id=el.id)
    except napravlen.DoesNotExist:
        vlk_n = None
    try:
        verific = verif.objects.filter(client_id=el.id)
    except verif.DoesNotExist:
        verific = None
    try:
        anketa = Anketa.objects.get(client_id=el.id)
    except Anketa.DoesNotExist:
        anketa = None
    if anketa is not None:
        time_close_ank = anketa.last_modified > anketa.created
    else:
        time_close_ank = False

    try:
        vlk = vlk_napr.objects.get(client_id=el.id)
    except vlk_napr.DoesNotExist:
        vlk = None

    try:
        close_edit = zgoda_bat.objects.get(client_id=el.id)
    except zgoda_bat.DoesNotExist:
        close_edit = None
    if close_edit is not None:
        time_close = close_edit.last_modified > close_edit.created
    else:
        time_close = False

    try:
        close_edit6 = Med.objects.get(client_id=el.id)
    except Med.DoesNotExist:
        close_edit6 = None
    if close_edit6 is not None:
        time_close_med = close_edit6.last_modified > close_edit6.created
    else:
        time_close_med = False

    try:
        close_edit1 = documents.objects.get(client_id=el.id)
    except documents.DoesNotExist:
        close_edit1 = None
    if close_edit1 is not None:
        time_close1 = close_edit1.last_modified > close_edit1.created
    else:
        time_close1 = False
    try:
        close_edit2 = corup.objects.get(client_id=el.id)
    except corup.DoesNotExist:
        close_edit2 = None
    if close_edit2 is not None:
        time_close2 = close_edit2.last_modified > close_edit2.created
    else:
        time_close2 = False
    try:
        med = Med.objects.get(client_id=el.id)
    except Med.DoesNotExist:
        med = None

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
    anket = cur.fetchone()[0] > 0
    cur.execute("SELECT COUNT(*) FROM main_verificate_photo_client WHERE client_id=%s", (el.id, ))
    ve = cur.fetchone()[0] > 0
    cur.execute("SELECT COUNT(*) FROM main_zgoda_bat WHERE client_id=%s", (el.id, ))
    zgodbat = cur.fetchone()[0] > 0
    cur.execute("SELECT COUNT(*) FROM main_corup WHERE client_id=%s", (el.id, ))
    co = cur.fetchone()[0] > 0
    cur.execute("SELECT COUNT(*) FROM main_documents WHERE client_id=%s", (el.id, ))
    do = cur.fetchone()[0] > 0
    cur.execute("SELECT COUNT(*) FROM main_med WHERE client_id=%s",(el.id, ))
    meds = cur.fetchone()[0] > 0
    tf = Mod_TF.objects.filter(client_id=el.id).first()
    v = verif.objects.filter(client_id=el.id).first()

    return render(request, 'main/cabinet.html', {
        'el': el,
        'za': za,
        'anket': anket,
        'd': el2,
        've': ve,
        'zgodbat': zgodbat,
        'co': co,
        'do': do,
        'meds': meds,
        'tf': tf,
        'v': v,
        'dozvil': dozvil,
        "red": red,
        'time_close': time_close,
        'time_close1': time_close1,
        'time_close2': time_close2,
        'verific': verific,
        'anketa': anketa,
        'close_edit1': close_edit1,
        'close_edit': close_edit,
        'close_edit2': close_edit,
        'med': med,
        'vlk': vlk,
        'vlk_n': vlk_n,
        'vid_napr': vid_napr,
        'time_close_ank': time_close_ank,
        'time_close_med': time_close_med
    })


