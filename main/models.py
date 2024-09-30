from django.db import models
from django.utils import timezone
import django_filters


class Clients(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Moderator(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Sing_Clients(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    soname = models.CharField(max_length=1024)
    fname = models.CharField(max_length=1024)
    name2 = models.CharField(max_length=1024)
    soname2 = models.CharField(max_length=1024)
    fname2 = models.CharField(max_length=1024)
    email = models.EmailField(max_length=1024)
    military = models.CharField(max_length=1024, null=True, blank=True)
    date = models.CharField(max_length=1024)
    born = models.CharField(max_length=1024)
    document = models.CharField(max_length=1024)
    num = models.CharField(max_length=1024)
    lang = models.CharField(max_length=1024)
    pogad = models.CharField(verbose_name='Погоджуюсь')
    place_med = models.CharField(max_length=1024)
    sex = models.CharField(max_length=5)
    data_now2 = models.DateTimeField(auto_now_add=True)


class nadatu_dozvil(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='nadatu_dozvil2')
    anketa_dozvil = models.CharField(max_length=1024, null=True, blank=True)
    corup_dozvil = models.CharField(max_length=1024, null=True, blank=True)
    zgoda_dozvil = models.CharField(max_length=1024, null=True, blank=True)
    documents_dozvil = models.CharField(max_length=1024, null=True, blank=True)
    med_dozvil = models.CharField(max_length=1024, null=True, blank=True)


class vid_red(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='vid_red2')
    anketa_red = models.CharField(max_length=1024, null=True, blank=True)
    corup_red = models.CharField(max_length=1024, null=True, blank=True)
    zgoda_bat_red = models.CharField(max_length=1024, null=True, blank=True)
    documents_red = models.CharField(max_length=1024, null=True, blank=True)
    med_red = models.CharField(max_length=1024, null=True, blank=True)


class verif(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='verif')
    verify_client = models.CharField(max_length=10, null=True, blank=True)


class verificate_photo_client(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='verify2')
    photo1 = models.ImageField(upload_to='media/main/ver')


class Mod_TF(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='mod_tf')
    tf1 = models.BooleanField(default=False, max_length=10, null=True, blank=True)
    tf2 = models.BooleanField(default=False, null=True, blank=True)
    tf3 = models.BooleanField(default=False, null=True, blank=True)
    tf4 = models.BooleanField(default=False, null=True, blank=True)
    tf5 = models.BooleanField(default=False, null=True, blank=True)
    tf6 = models.BooleanField(default=False, null=True, blank=True)
    tf7 = models.BooleanField(default=False, null=True, blank=True)

    tfe1 = models.BooleanField(default=False, null=True, blank=True)
    tfe2 = models.BooleanField(default=False, null=True, blank=True)
    tfe3 = models.BooleanField(default=False, null=True, blank=True)
    tfe4 = models.BooleanField(default=False, null=True, blank=True)
    tfe5 = models.BooleanField(default=False, null=True, blank=True)


class napravlen(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='napravl')
    true_false = models.CharField(max_length=1024)


class Anketa_draft(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='Anketa_dtaft')
    photo = models.ImageField(upload_to='media/main/Anketa')#
    nsf = models.CharField(max_length=1024)#1
    count = models.IntegerField(default=0, null=True, blank=True)
    ed_nsf = models.CharField(max_length=1024)#2
    born = models.CharField(max_length=1024)#3
    place = models.CharField(max_length=1024)#4
    place_register = models.CharField(max_length=1024)#5
    place_live = models.CharField(max_length=1024)#6
    cityzen = models.CharField(max_length=1024)#7
    edit_cit = models.CharField(max_length=1024)#8
    pasport = models.CharField(max_length=1024)#9
    pasport_c = models.CharField(max_length=1024)#10
    en_doc = models.CharField(max_length=1024)#11
    education = models.CharField(max_length=1024)#12
    duplom = models.CharField(max_length=1024)#13
    len = models.CharField(max_length=1024)#14
    social_med = models.CharField(max_length=1024)#15
    tz = models.CharField(max_length=1024)#16
    zbroi = models.CharField(max_length=1024)#17
    crimanal = models.CharField(max_length=1024)#18
    teritory = models.CharField(max_length=1024)#19
    rf = models.CharField(max_length=1024)#20


    stupin = models.CharField(max_length=1024)
    name1 = models.CharField(max_length=1024)
    born1 = models.CharField(max_length=1024)
    work1 = models.CharField(max_length=1024)
    adress = models.CharField(max_length=1024)

    stupin2 = models.CharField(max_length=1024)
    name2 = models.CharField(max_length=1024)
    born2 = models.CharField(max_length=1024)
    work2 = models.CharField(max_length=1024)
    adress2 = models.CharField(max_length=1024)

    stupin3 = models.CharField(max_length=1024)
    name3 = models.CharField(max_length=1024)
    born3 = models.CharField(max_length=1024)
    work3 = models.CharField(max_length=1024)
    adress3 = models.CharField(max_length=1024)

    stupin4 = models.CharField(max_length=1024)
    name4 = models.CharField(max_length=1024)
    born4 = models.CharField(max_length=1024)
    work4 = models.CharField(max_length=1024)
    adress4 = models.CharField(max_length=1024)

    stupin5 = models.CharField(max_length=1024)
    name5 = models.CharField(max_length=1024)
    born5 = models.CharField(max_length=1024)
    work5 = models.CharField(max_length=1024)
    adress5 = models.CharField(max_length=1024)

    stupin6 = models.CharField(max_length=1024)
    name6 = models.CharField(max_length=1024)
    born6 = models.CharField(max_length=1024)
    work6 = models.CharField(max_length=1024)
    adress6 = models.CharField(max_length=1024)

    stupin7 = models.CharField(max_length=1024)
    name7 = models.CharField(max_length=1024)
    born7 = models.CharField(max_length=1024)
    work7 = models.CharField(max_length=1024)
    adress7 = models.CharField(max_length=1024)

    stupin8 = models.CharField(max_length=1024)
    name8 = models.CharField(max_length=1024)
    born8 = models.CharField(max_length=1024)
    work8 = models.CharField(max_length=1024)
    adress8 = models.CharField(max_length=1024)

    vstup = models.CharField(max_length=1024)
    zvil = models.CharField(max_length=1024)
    posada = models.CharField(max_length=1024)
    location = models.CharField(max_length=1024)

    vstup1 = models.CharField(max_length=1024)
    zvil1 = models.CharField(max_length=1024)
    posada1 = models.CharField(max_length=1024)
    location1 = models.CharField(max_length=1024)

    vstup2 = models.CharField(max_length=1024)
    zvil2 = models.CharField(max_length=1024)
    posada2 = models.CharField(max_length=1024)
    location2 = models.CharField(max_length=1024)

    vstup4 = models.CharField(max_length=1024)
    zvil4 = models.CharField(max_length=1024)
    posada4 = models.CharField(max_length=1024)
    location4 = models.CharField(max_length=1024)

    vstup5 = models.CharField(max_length=1024)
    zvil5 = models.CharField(max_length=1024)
    posada5 = models.CharField(max_length=1024)
    location5 = models.CharField(max_length=1024)

    seria_num = models.CharField(max_length=1024)
    kum = models.CharField(max_length=1024)
    kontact_sl = models.CharField(max_length=1024)
    kontact_os = models.CharField(max_length=1024)
    kontact_fa = models.CharField(max_length=1024)
    kontact_ma = models.CharField(max_length=1024)
    data22 = models.CharField(max_length=1024, null=True, blank=True)
    data_now = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Anketa(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='Anketa')
    photo = models.ImageField(upload_to='media/main/Anketa')#
    nsf = models.CharField(max_length=1024)#1
    ed_nsf = models.CharField(max_length=1024)#2
    born = models.CharField(max_length=1024)#3
    place = models.CharField(max_length=1024)#4
    place_register = models.CharField(max_length=1024)#5
    place_live = models.CharField(max_length=1024)#6
    cityzen = models.CharField(max_length=1024)#7
    edit_cit = models.CharField(max_length=1024)#8
    pasport = models.CharField(max_length=1024)#9
    pasport_c = models.CharField(max_length=1024)#10
    en_doc = models.CharField(max_length=1024)#11
    education = models.CharField(max_length=1024)#12
    duplom = models.CharField(max_length=1024)#13
    len = models.CharField(max_length=1024)#14
    social_med = models.CharField(max_length=1024)#15
    tz = models.CharField(max_length=1024)#16
    zbroi = models.CharField(max_length=1024)#17
    crimanal = models.CharField(max_length=1024)#18
    teritory = models.CharField(max_length=1024)#19
    rf = models.CharField(max_length=1024)#20

    stupin = models.CharField(max_length=1024)
    name1 = models.CharField(max_length=1024)
    born1 = models.CharField(max_length=1024)
    work1 = models.CharField(max_length=1024)
    adress = models.CharField(max_length=1024)

    stupin2 = models.CharField(max_length=1024)
    name2 = models.CharField(max_length=1024)
    born2 = models.CharField(max_length=1024)
    work2 = models.CharField(max_length=1024)
    adress2 = models.CharField(max_length=1024)

    stupin3 = models.CharField(max_length=1024)
    name3 = models.CharField(max_length=1024)
    born3 = models.CharField(max_length=1024)
    work3 = models.CharField(max_length=1024)
    adress3 = models.CharField(max_length=1024)

    stupin4 = models.CharField(max_length=1024)
    name4 = models.CharField(max_length=1024)
    born4 = models.CharField(max_length=1024)
    work4 = models.CharField(max_length=1024)
    adress4 = models.CharField(max_length=1024)

    stupin5 = models.CharField(max_length=1024)
    name5 = models.CharField(max_length=1024)
    born5 = models.CharField(max_length=1024)
    work5 = models.CharField(max_length=1024)
    adress5 = models.CharField(max_length=1024)

    stupin6 = models.CharField(max_length=1024)
    name6 = models.CharField(max_length=1024)
    born6 = models.CharField(max_length=1024)
    work6 = models.CharField(max_length=1024)
    adress6 = models.CharField(max_length=1024)

    stupin7 = models.CharField(max_length=1024)
    name7 = models.CharField(max_length=1024)
    born7 = models.CharField(max_length=1024)
    work7 = models.CharField(max_length=1024)
    adress7 = models.CharField(max_length=1024)

    stupin8 = models.CharField(max_length=1024)
    name8 = models.CharField(max_length=1024)
    born8 = models.CharField(max_length=1024)
    work8 = models.CharField(max_length=1024)
    adress8 = models.CharField(max_length=1024)

    vstup = models.CharField(max_length=1024)
    zvil = models.CharField(max_length=1024)
    posada = models.CharField(max_length=1024)
    location = models.CharField(max_length=1024)

    vstup1 = models.CharField(max_length=1024)
    zvil1 = models.CharField(max_length=1024)
    posada1 = models.CharField(max_length=1024)
    location1 = models.CharField(max_length=1024)

    vstup2 = models.CharField(max_length=1024)
    zvil2 = models.CharField(max_length=1024)
    posada2 = models.CharField(max_length=1024)
    location2 = models.CharField(max_length=1024)

    vstup4 = models.CharField(max_length=1024)
    zvil4 = models.CharField(max_length=1024)
    posada4 = models.CharField(max_length=1024)
    location4 = models.CharField(max_length=1024)

    vstup5 = models.CharField(max_length=1024)
    zvil5 = models.CharField(max_length=1024)
    posada5 = models.CharField(max_length=1024)
    location5 = models.CharField(max_length=1024)

    seria_num = models.CharField(max_length=1024)
    kum = models.CharField(max_length=1024)
    kontact_sl = models.CharField(max_length=1024)
    kontact_os = models.CharField(max_length=1024)
    kontact_fa = models.CharField(max_length=1024)
    kontact_ma = models.CharField(max_length=1024)
    data22 = models.CharField(max_length=1024)
    data_now = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class re_password(models.Model):
    email = models.CharField(max_length=1024, null=True, blank=True)
    code = models.CharField(max_length=8, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)


class documents(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='documents')
    id_card = models.ImageField(upload_to='media/main/doc')
    id_card2 = models.ImageField(upload_to='media/main/doc')
    location_doc = models.ImageField(upload_to='media/main/doc')
    born_doc = models.ImageField(upload_to='media/main/doc')
    plat_doc = models.ImageField(upload_to='media/main/doc')
    spec_doc = models.ImageField(upload_to='media/main/doc')
    photo_doc = models.ImageField(upload_to='media/main/doc')
    cruminal_doc = models.ImageField(upload_to='media/main/doc')
    psix_doc = models.ImageField(upload_to='media/main/doc')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Filter(django_filters.FilterSet):
    soname = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Anketa
        fields = ['soname',]


class Med(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='Med')
    pos_v = models.CharField(max_length=1024, null=True)
    psix = models.CharField(max_length=1024)
    protu_tub = models.CharField(max_length=1024)
    antutila = models.CharField(max_length=1024)
    skira = models.CharField(max_length=1024)
    f025 = models.CharField(max_length=1024)
    f027 = models.CharField(max_length=1024)
    f063 = models.CharField(max_length=1024)

    an_kr = models.CharField(max_length=1024, null=True, blank=True)
    an_s = models.CharField(max_length=1024, null=True, blank=True)
    bio_h = models.CharField(max_length=1024, null=True, blank=True)
    ser_an_k = models.CharField(max_length=1024, null=True, blank=True)
    ant_b = models.CharField(max_length=1024, null=True, blank=True)
    ant_c = models.CharField(max_length=1024, null=True, blank=True)
    rw = models.CharField(max_length=1024, null=True, blank=True)
    flu = models.CharField(max_length=1024, null=True, blank=True)
    ekg = models.CharField(max_length=1024, null=True, blank=True)

    data = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class corup(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='corup')
    f22 = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class zgoda_bat(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='zgoda')
    photo_zgodu = models.ImageField(upload_to='media/main/zgoda_bat')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class vlk_napr(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='vlk')
    pdf = models.FileField(upload_to='main/vlk_napr')

class Moder_napr(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='moder_napr')
    napr_img = models.ImageField(upload_to='media/main/pdf_moder_napr')


class check_napr(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='check_napr2')
    check2 = models.CharField(max_length=24)