from django.http import HttpResponseNotFound
from django.urls import path, re_path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .import (cabinet, Login_logout, Anketa, Anketa_edit,
              edit_password, upload_photo_verification,
              moderator_verif_client, pdf_zayava, pdf_anketa,
              documents, documents_edit, moderator, pdf_zgoda,
              zgoda_bat, zgoda_bat_edit, coruption_edit, coruption,
              pdf_coruption, med_edit, med, Med_docs, zgoda_p, pdf_document,
              exel_data, open_zgoda, pdf_napravlen, vlk, vlk_nap_client, moderator_create, vid_red_doca,
              napr_otr, moder_vlknapr_vid, check_napr, json, ended
              )
from django.views.generic import RedirectView

from .models import corup

urlpatterns = [

    path('', views.index, name='home'),

    path('svbbghvfgdsfhfgdhhrttherghhy_234gnjtgtr_fnvbkfig433495jerg/', views.CreatUser, name='CreatUser'),
    path('wewewretchjbdnnbvvb_jvbrrijegti_923rfmrkniefonKNnNNjNKij/<int:id>', cabinet.Cabinet, name='cabinet'),
    path('sdfergEGRfbgnfcxsGTBDFbvbfmh_kmefvnjbhBBBhbubGV8347/<int:id>', vid_red_doca.red_zaput, name='red_zaput'),
    path('ghbfhnbhfhfbggbhhnbhfg/<int:id>', napr_otr.otr_napr, name='napr_otr'),
    path('aghdj46645dfgdhvb_gfGF34vgij_jhc#$56ygfh/<int:id>', moder_vlknapr_vid.moder_vlknapr_vid, name='vid_napr'),
    path('wy4uHJH426H447323Hbb48374pkdnfnrkrerj_fnfe(hjddj0djdj_/<int:id>', napr_otr.moder_napr_otr, name='moders_napr_otr'),
    path('wy4uHJH42byjytrtgref5r6u56tyvcgnfnrkrerj_fnfe(hjddj0djdj_/<int:id>', check_napr.check_napravlen,name='check_napravlen'),

    path('svbbghv342ergrrtgdffe645rvftgtr_ghdt32jerg/', views.CreatUser, name='CreatUser'),

    path('dgshvrhbjbv_ejrghhjf_7ryjebhJHUBlook284r7wdievnf/', Login_logout.login, name='login'),
    path('byffvbbvjmlkbhvnvnbvfbghfj_flbmewfkmd23KI-0okdco09dwcei)qdcwn/', Login_logout.logout_view, name='logout'),

    path('ngmknubvhjbvhg_46752hd_fbc24637435_fbhgfevug/<int:id>', Anketa.anketa, name='anketa'),
    path('bvdhbvfdghgvcfvbbh_njgfbgbdhjdsbfdshjfbds/<int:id>', Anketa_edit.edit_anketa, name='edit_anketa'),

    path('huusfdshsfsbdfhbf_fnjgbehg_45y_fdshb/', edit_password.restore_password, name='restore_password'),
    path('thrgehsdfhdhdfghfhdh_fhdbfvgdsjkksd_jdjd22/', edit_password.restore_password2, name='password2'),
    path('hbfbgbvhbxcvbnnytqaertp_fbvvbfvdvjnvsdj/', edit_password.edit_password, name='edit_password'),

    path('fdcbgvvggvhvgvghj_jdhdduwwmnv/<int:id>', upload_photo_verification.verify2, name='verify'),

    path('ghjhnmnbvb_cgvhbjnbvcxzv/<int:id>', moderator_verif_client.aut3, name='aut'),
    path('gbhmjvcfchbgfhj_1dfgh34fnbdhffbcd/<int:id>', moderator_verif_client.ver, name='ver'),


    path('stdnfbmbfgh_plfcgthgfb/<int:id>', pdf_zayava.Download_PDF, name='down_pdf'),
    path('vbgfjfdcgbdgvdf_dfhcbdxnqaxhjcc/<int:id>', pdf_zayava.creat, name='create'),


    path('bvjyhvgnukbkv_hcafdnsgvffv/<int:id>', pdf_anketa.generate_pdf, name='generate_pdf'),

    path('evrstrhyvzghbbvhbvhgbvgf_jkcghhdhfcadcscg/<int:id>', documents.document, name='document'),
    path('gfbghhhghj_qwertryu467hgfvdcvnm/<int:id>', documents_edit.edit_document, name='edit_document'),

    path('dsrsvdbfyuuknunybvbfbgvhfbnnmh_mkbhvcfghvbnmnbvgfgfbehrjtkuyuytr/<int:id>', moderator.moderator, name='moderator'),
    path('btvhfbgnhjkhgbfg_rujdmxmxmc45_jfb54/<int:id>', moderator.items, name='items'),
    path('qadfgvbnoljhgf_jhgsfdv234_dhfdcg/<int:id>', moderator.save_dozvil_data, name='save_dozvil_data'),

    path('etrbtrdybvdhn_bsdhvbvvbvhb_97044_vsdfvgbgf/<int:id>', pdf_zgoda.generate_zgoda, name='generate_zgoda'),
    path('gvdfbvxzzxcvbnmuyt_dgxbjdjskjfh/<int:id>', zgoda_bat.zgoda_ofor, name='zgoda_ofor'),
    path('fddbhjhvgscxzdfxnm_ef2h9dhf/<int:id>', zgoda_bat_edit.edit_zgoda, name='edit_zgoda'),

    path('tbyjhvjbfmnbghgdfgghfj_ejeghcfjc_38746hjbdfdn/<int:id>', coruption.corupt, name='corup'),
    path('ghjchghg,bjghgfvfffgybv_ijgvhcjr_v/<int:id>', coruption_edit.edit_cor, name='edit_cor'),
    path('bjfyhcfgfhjnvjhbjgfvd_hfgvcjfkddc_487rdhjfgfd/<int:id>', pdf_coruption.generate_cor, name='generate_cor'),

    path('bhgdfnu3ymi3hgubytz2x_cgvbxjncjhb1n3467fckdvjfhb/<int:id>', med.med, name='med'),
    path('fsntbj23jybt7umnkbjhbhbb7n5bbhvhbhbfh/<int:id>', med_edit.edit_med, name='edit_med'),
    path('ghfbgmjghvv6vfgbnhbhvfb56_ijifvghcur/<int:id>', Med_docs.med_docs, name='med_docs'),
    path('sfodnbgthrfdngfbidjfgnkbtdjgnb/', open_zgoda.open_pdf, name='open_zgoda'),

    path('gfhbjhgvgfh_adjsbg4nfdjk47thertgvbn/<int:id>', zgoda_p.download_zgoda_p, name='download_zgoda_p'),

    path('dfbghbhjghfbhvgfvg/<int:id>', pdf_document.generate_doc, name='generate_doc'),

    path('rsbdstgfdghvbhfjbfv_fbgvh/', exel_data.exel_data, name='exel'),

    path('vhtgbnhgtrftghvb_wgfvbnh/', open_zgoda.open_pdf, name='open_pdf'),

    path('dfehtjfgjhbbghkjggujkykkuj/<int:id>', ended.ended, name='ended_ank'),

    path('fvdbydvtfv_ghhnjbfvbdv/<int:id>', pdf_napravlen.download_PDF, name='download_PDF_napravlen'),

    path('tjytvbd)rgvbv_vbhndgbvhtvbsvhgvg/<int:id>', vlk.vlkN, name='vlk_n'),
    path('fdbsvhbvfdgfgvf-vsvgdvfcgv5tvlk/<int:id>', vlk_nap_client.download_pdf, name='download_pdf'),

    path('asdfgnhnhmfgcbnhfdfhredrtrbrvtcgrtsdgdhtjyds_frgbthfddnbbijfkfn/', moderator_create.ModeratorCreate, name='moderator_create'),
    path('asrdsdjjhcrerxcbvdhtrybvcgetvctbhvvrertvrvbytcsvcg_egyrepfkdnqnsmxdkfbfjffdm/', moderator_create.moderator_login, name='moderator_login'),

    path('not_found', views.page_not_found, name='your-redirect-page'),
    path('redirect-page', views.page_not_found, name='redirect-page'),

    path('ws/json/<int:id>/', json.json_request_ver, name='json_request'),
    path('json/ank/<int:id>/', json.json_request_tf, name='json_tf'),
    path('ws/corup/<int:id>/', json.json_request_tf5, name='json_tf5'),
    path('ws/corup4/<int:id>/', json.json_request_tf4, name='json_tf4'),
    path('ws/med6/<int:id>/', json.json_request_tf6, name='json_tf6'),
    path('ws/doc7/<int:id>/', json.json_request_tf7, name='json_tf7'),
    path('ws/vlk/<int:id>/', json.json_vlk, name='json_vlk'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


