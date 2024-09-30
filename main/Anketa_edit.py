from django.http import HttpResponseForbidden

from .models import Clients, Anketa, Anketa_draft
from django.shortcuts import render, redirect, get_object_or_404

def edit_anketa(request, id):
    el = Clients.objects.get(id=id)
    info = Anketa_draft.objects.filter(client_id=el.id)
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    obj1 = get_object_or_404(Anketa, client_id=el.id)
    if request.method == 'POST':
        photo = request.FILES['photo']
        nsf = request.POST['nsf']
        ed_nsf = request.POST['ed_nsf']
        born = request.POST['born']
        place = request.POST['place']
        place_register = request.POST['place_register']
        place_live = request.POST['place_live']
        cityzen = request.POST['cityzen']
        edit_cit = request.POST['edit_cit']
        pasport = request.POST['pasport']
        pasport_c = request.POST['pasport_c']
        en_doc = request.POST['en_doc']
        education = request.POST['education']
        duplom = request.POST['duplom']
        len = request.POST['len']
        social_med = request.POST['social_med']
        tz = request.POST['tz']
        zbroi = request.POST['zbroi']
        crimanal = request.POST['crimanal']
        teritory = request.POST['teritory']
        rf = request.POST['rf']

        stupin = request.POST['stupin']
        name1 = request.POST['name1']
        born1 = request.POST['born1']
        work1 = request.POST['work1']
        adress = request.POST['adress']

        stupin2 = request.POST['stupin2']
        name2 = request.POST['name2']
        born2 = request.POST['born2']
        work2 = request.POST['work2']
        adress2 = request.POST['adress2']

        stupin3 = request.POST['stupin3']
        name3 = request.POST['name3']
        born3 = request.POST['born3']
        work3 = request.POST['work3']
        adress3 = request.POST['adress3']

        stupin4 = request.POST['stupin4']
        name4 = request.POST['name4']
        born4 = request.POST['born4']
        work4 = request.POST['work4']
        adress4 = request.POST['adress4']

        stupin5 = request.POST['stupin5']
        name5 = request.POST['name5']
        born5 = request.POST['born5']
        work5 = request.POST['work5']
        adress5 = request.POST['adress5']

        stupin6 = request.POST['stupin6']
        name6 = request.POST['name6']
        born6 = request.POST['born6']
        work6 = request.POST['work6']
        adress6 = request.POST['adress6']

        stupin7 = request.POST['stupin7']
        name7 = request.POST['name7']
        born7 = request.POST['born7']
        work7 = request.POST['work7']
        adress7 = request.POST['adress7']

        stupin8 = request.POST['stupin8']
        name8 = request.POST['name8']
        born8 = request.POST['born8']
        work8 = request.POST['work8']
        adress8 = request.POST['adress8']

        vstup = request.POST['vstup']
        zvil = request.POST['zvil']
        posada = request.POST['posada']
        location = request.POST['location']

        vstup1 = request.POST['vstup1']
        zvil1 = request.POST['zvil1']
        posada1 = request.POST['posada1']
        location1 = request.POST['location1']

        vstup2 = request.POST['vstup2']
        zvil2 = request.POST['zvil2']
        posada2 = request.POST['posada2']
        location2 = request.POST['location2']

        vstup4 = request.POST['vstup4']
        zvil4 = request.POST['zvil4']
        posada4 = request.POST['posada4']
        location4 = request.POST['location4']

        vstup5 = request.POST['vstup5']
        zvil5 = request.POST['zvil5']
        posada5 = request.POST['posada5']
        location5 = request.POST['location5']

        seria_num = request.POST['seria_num']
        kum = request.POST['kum']
        kontact_sl = request.POST['kontact_sl']
        kontact_os = request.POST['kontact_os']
        kontact_fa = request.POST['kontact_fa']
        kontact_ma = request.POST['kontact_ma']
        data22 = request.POST['data22']

        obj1.photo = photo
        obj1.nsf = nsf
        obj1.ed_nsf = ed_nsf
        obj1.born = born
        obj1.place = place
        obj1.place_register = place_register
        obj1.place_live = place_live
        obj1.cityzen = cityzen
        obj1.edit_cit = edit_cit
        obj1.pasport = pasport
        obj1.pasport_c = pasport_c
        obj1.en_doc = en_doc
        obj1.education = education
        obj1.duplom = duplom
        obj1.len = len
        obj1.social_med = social_med
        obj1.tz = tz
        obj1.zbroi = zbroi
        obj1.crimanal = crimanal
        obj1.teritory = teritory
        obj1.rf = rf
        obj1.stupin = stupin
        obj1.name1 = name1
        obj1.born1 = born1
        obj1.work1 = work1
        obj1.adress = adress
        obj1.stupin2 = stupin2
        obj1.name2 = name2
        obj1.born2 = born2
        obj1.work2 = work2
        obj1.adress2 = adress2
        obj1.stupin3 = stupin3
        obj1.name3 = name3
        obj1.born3 = born3
        obj1.work3 = work3
        obj1.adress3 =adress3
        obj1.stupin3 = stupin3
        obj1.name3 = name3
        obj1.born3 = born3
        obj1.work3 = work3
        obj1.adress3 = adress3
        obj1.stupin4 = stupin4
        obj1.name4 = name4
        obj1.born4 = born4
        obj1.work4 = work4
        obj1.adress4 = adress4
        obj1.stupin5 = stupin5
        obj1.name5 = name5
        obj1.born5 = born5
        obj1.work5 = work5
        obj1.adress5 = adress5
        obj1.stupin6 = stupin6
        obj1.name6 = name6
        obj1.born6 = born6
        obj1.work6 = work6
        obj1.adress6 = adress6
        obj1.stupin7 = stupin7
        obj1.name7 = name7
        obj1.born7 = born7
        obj1.work7 = work7
        obj1.adress7 = adress7
        obj1.stupin8 = stupin8
        obj1.name8 = name8
        obj1.born8 = born8
        obj1.work8 = work8
        obj1.adress8 = adress8

        obj1.vstup = vstup
        obj1.zvil = zvil
        obj1.posada = posada
        obj1.location = location

        obj1.vstup1 = vstup1
        obj1.zvil1 = zvil1
        obj1.posada1 = posada1
        obj1.location1 = location1

        obj1.vstup2 = vstup2
        obj1.zvil2 = zvil2
        obj1.posada2 = posada2
        obj1.location2 = location2

        obj1.vstup4 = vstup4
        obj1.zvil4 = zvil4
        obj1.posada4 = posada4
        obj1.location4 = location4
        obj1.vstup5 = vstup5
        obj1.zvil5 = zvil5
        obj1.posada5 = posada5
        obj1.location5 = location5

        obj1.seria_num = seria_num
        obj1.kum = kum
        obj1.kontact_sl = kontact_sl
        obj1.kontact_os = kontact_os
        obj1.kontact_fa =kontact_fa
        obj1.kontact_ma =kontact_ma
        obj1.data22 = data22
        obj1.save()
        return redirect('cabinet', id=id)
    else:
        edit = {
            'photo': obj1.photo,
            'nsf': obj1.nsf,
            'ed_nsf': obj1.ed_nsf,
            'born': obj1.born,
            'place': obj1.place,
            'place_register': obj1.place_register,
            'place_live': obj1.place_live,
            'cityzen': obj1.cityzen,
            'edit_cit': obj1.edit_cit,
            'pasport': obj1.pasport,
            'pasport_c': obj1.pasport_c,
            'en_doc': obj1.en_doc,
            'education': obj1.education,
            'duplom': obj1.duplom,
            'len': obj1.len,
            'social_med': obj1.social_med,
            'tz': obj1.tz,
            'zbroi': obj1.zbroi,
            'crimanal': obj1.crimanal,
            'teritory': obj1.teritory,
            'rf': obj1.rf,
            'stupin': obj1.stupin,
            'name1': obj1.name1,
            'born1': obj1.born1,
            'work1': obj1.work1,
            'adress': obj1.adress,

            'stupin3': obj1.stupin3,
            'name3': obj1.name3,
            'born3': obj1.born3,
            'work3': obj1.work3,
            'adress3': obj1.adress3,

            'stupin4': obj1.stupin4,
            'name4': obj1.name4,
            'born4': obj1.born4,
            'work4': obj1.work4,
            'adress4': obj1.adress4,

            'stupin5': obj1.stupin5,
            'name5': obj1.name5,
            'born5': obj1.born5,
            'work5': obj1.work5,
            'adress5': obj1.adress5,

            'stupin6': obj1.stupin6,
            'name6': obj1.name6,
            'born6': obj1.born6,
            'work6': obj1.work6,
            'adress6': obj1.adress6,

            'stupin7': obj1.stupin7,
            'name7': obj1.name7,
            'born7': obj1.born7,
            'work7': obj1.work7,
            'adress7': obj1.adress7,

            'stupin8': obj1.stupin8,
            'name8': obj1.name8,
            'born8': obj1.born8,
            'work8': obj1.work8,
            'adress8': obj1.adress8,

            'vstup': obj1.vstup,
            'zvil': obj1.zvil,
            'posada': obj1.posada,
            'location': obj1.location,

            'vstup1': obj1.vstup1,
            'zvil1': obj1.zvil1,
            'posada1': obj1.posada1,
            'location1': obj1.location1,

            'vstup2': obj1.vstup2,
            'zvil2': obj1.zvil2,
            'posada2': obj1.posada2,
            'location2': obj1.location2,

            'vstup4': obj1.vstup4,
            'zvil4': obj1.zvil4,
            'posada4': obj1.posada4,
            'location4': obj1.location4,

            'vstup5': obj1.vstup5,
            'zvil5': obj1.zvil5,
            'posada5': obj1.posada5,
            'location5': obj1.location5,

            'seria_num': obj1.seria_num,
            'kum': obj1.kum,
            'kontact_sl': obj1.kontact_sl,
            'kontact_os': obj1.kontact_os,
            'kontact_fa': obj1.kontact_fa,
            'kontact_ma': obj1.kontact_ma,
            'data22': obj1.data22,
        }
    return render(request, 'main/edit_anketa.html', {'edit': edit, 'info': info})

