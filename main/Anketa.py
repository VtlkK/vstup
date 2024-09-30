from django.http import HttpResponseForbidden

from .models import Clients, Anketa, Anketa_draft
from django.shortcuts import render, redirect, get_object_or_404

def anketa(request, id):
    el = Clients.objects.get(id=id)
    ank_list = Anketa_draft.objects.filter(client_id=el.id)
    if ank_list.exists():
        ank = ank_list.first()
        if request.method == 'POST' and 'save2' in request.POST:
            if ank.count < 3:
                ank.count += 1
                ank.save()
        show_save_button = ank.count < 3
    else:
        ank = None
        show_save_button = True
    idd = request.session.get('id')
    if idd is None or int(idd) != int(el.id):
        return HttpResponseForbidden("У вас немає доступу до цієї сторінки.")
    if Anketa.objects.filter(client_id=el.id).exists():
        return redirect('cabinet', id=el.id)
    if request.method == 'POST':
        photo = request.FILES.get('photo')
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

        if 'save' in request.POST:
            obj1 = Anketa(
                client=el,
                photo=photo, nsf=nsf, ed_nsf=ed_nsf, born=born, place=place,
                place_register=place_register, place_live=place_live, cityzen=cityzen,
                edit_cit=edit_cit, pasport=pasport, pasport_c=pasport_c, en_doc=en_doc,
                education=education, duplom=duplom, len=len, social_med=social_med, tz=tz,
                zbroi=zbroi, crimanal=crimanal, teritory=teritory, rf=rf,
                stupin=stupin, name1=name1, born1=born1, work1=work1, adress=adress,
                stupin2=stupin2, name2=name2, born2=born2, work2=work2, adress2=adress2,
                stupin3=stupin3, name3=name3, born3=born3, work3=work3, adress3=adress3,
                stupin4=stupin4, name4=name4, born4=born4, work4=work4, adress4=adress4,
                stupin5=stupin5, name5=name5, born5=born5, work5=work5, adress5=adress5,
                stupin6=stupin6, name6=name6, born6=born6, work6=work6, adress6=adress6,
                stupin7=stupin7, name7=name7, born7=born7, work7=work7, adress7=adress7,
                stupin8=stupin8, name8=name8, born8=born8, work8=work8, adress8=adress8,
                vstup=vstup, zvil=zvil, posada=posada, location=location,
                vstup1=vstup1, zvil1=zvil1, posada1=posada1, location1=location1,
                vstup2=vstup2, zvil2=zvil2, posada2=posada2, location2=location2,
                vstup4=vstup4, zvil4=zvil4, posada4=posada4, location4=location4,
                vstup5=vstup5, zvil5=zvil5, posada5=posada5, location5=location5,
                kum=kum,
                seria_num=seria_num, kontact_sl=kontact_sl, kontact_os=kontact_os, kontact_fa=kontact_fa,
                kontact_ma=kontact_ma, data22=data22
            )
            obj1.save()
            return redirect('cabinet', id=el.id)

        elif 'save2' in request.POST:
            obj2, created = Anketa_draft.objects.get_or_create(client=el)

            obj2.photo = request.POST.get('photo')

            obj2.nsf = request.POST.get('nsf')
            obj2.ed_nsf = request.POST.get('ed_nsf')
            obj2.born = request.POST.get('born')
            obj2.place = request.POST.get('place')
            obj2.place_register = request.POST.get('place_register')
            obj2.place_live = request.POST.get('place_live')
            obj2.cityzen = request.POST.get('cityzen')
            obj2.edit_cit = request.POST.get('edit_cit')
            obj2.pasport = request.POST.get('pasport')
            obj2.pasport_c = request.POST.get('pasport_c')
            obj2.en_doc = request.POST.get('en_doc')
            obj2.education = request.POST.get('education')
            obj2.duplom = request.POST.get('duplom')
            obj2.len = request.POST.get('len')
            obj2.social_med = request.POST.get('social_med')
            obj2.tz = request.POST.get('tz')
            obj2.zbroi = request.POST.get('zbroi')
            obj2.crimanal = request.POST.get('crimanal')
            obj2.teritory = request.POST.get('teritory')
            obj2.rf = request.POST.get('rf')

            obj2.stupin = request.POST.get('stupin')
            obj2.name1 = request.POST.get('name1')
            obj2.born1 = request.POST.get('born1')
            obj2.work1 = request.POST.get('work1')
            obj2.adress = request.POST.get('adress')

            obj2.stupin2 = request.POST.get('stupin2')
            obj2.name2 = request.POST.get('name2')
            obj2.born2 = request.POST.get('born2')
            obj2.work2 = request.POST.get('work2')
            obj2.adress2 = request.POST.get('adress2')

            obj2.stupin3 = request.POST.get('stupin3')
            obj2.name3 = request.POST.get('name3')
            obj2.born3 = request.POST.get('born3')
            obj2.work3 = request.POST.get('work3')
            obj2.adress3 = request.POST.get('adress3')

            obj2.stupin4 = request.POST.get('stupin4')
            obj2.name4 = request.POST.get('name4')
            obj2.born4 = request.POST.get('born4')
            obj2.work4 = request.POST.get('work4')
            obj2.adress4 = request.POST.get('adress4')

            obj2.stupin5 = request.POST.get('stupin5')
            obj2.name5 = request.POST.get('name5')
            obj2.born5 = request.POST.get('born5')
            obj2.work5 = request.POST.get('work5')
            obj2.adress5 = request.POST.get('adress5')

            obj2.stupin6 = request.POST.get('stupin6')
            obj2.name6 = request.POST.get('name6')
            obj2.born6 = request.POST.get('born6')
            obj2.work6 = request.POST.get('work6')
            obj2.adress6 = request.POST.get('adress6')

            obj2.stupin7 = request.POST.get('stupin7')
            obj2.name7 = request.POST.get('name7')
            obj2.born7 = request.POST.get('born7')
            obj2.work7 = request.POST.get('work7')
            obj2.adress7 = request.POST.get('adress7')

            obj2.stupin8 = request.POST.get('stupin8')
            obj2.name8 = request.POST.get('name8')
            obj2.born8 = request.POST.get('born8')
            obj2.work8 = request.POST.get('work8')
            obj2.adress8 = request.POST.get('adress8')

            obj2.vstup = request.POST.get('vstup')
            obj2.zvil = request.POST.get('zvil')
            obj2.posada = request.POST.get('posada')
            obj2.location = request.POST.get('location')

            obj2.vstup1 = request.POST.get('vstup1')
            obj2.zvil1 = request.POST.get('zvil1')
            obj2.posada1 = request.POST.get('posada1')
            obj2.location1 = request.POST.get('location1')

            obj2.vstup2 = request.POST.get('vstup2')
            obj2.zvil2 = request.POST.get('zvil2')
            obj2.posada2 = request.POST.get('posada2')
            obj2.location2 = request.POST.get('location2')

            obj2.vstup4 = request.POST.get('vstup4')
            obj2.zvil4 = request.POST.get('zvil4')
            obj2.posada4 = request.POST.get('posada4')
            obj2.location4 = request.POST.get('location4')

            obj2.vstup5 = request.POST.get('vstup5')
            obj2.zvil5 = request.POST.get('zvil5')
            obj2.posada5 = request.POST.get('posada5')
            obj2.location5 = request.POST.get('location5')

            obj2.seria_num = request.POST.get('seria_num')
            obj2.kum = request.POST.get('kum')
            obj2.kontact_sl = request.POST.get('kontact_sl')
            obj2.kontact_os = request.POST.get('kontact_os')
            obj2.kontact_fa = request.POST.get('kontact_fa')
            obj2.kontact_ma = request.POST.get('kontact_ma')
            obj2.data22 = request.POST.get('data22')

            obj2.save()
            return redirect('cabinet', id=el.id)

    return render(request, 'main/anketa.html', {'ank': ank, 'show_save_button': show_save_button})

