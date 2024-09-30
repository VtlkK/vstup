import os
from django.shortcuts import HttpResponse
from django.views.decorators.cache import never_cache

@never_cache
def open_pdf(request):
    pdf_path = os.path.join('main', 'pdf', 'zgoda_p1.pdf')

    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="Згода.pdf"'
            return response
    else:
        return HttpResponse('Файл не знайдено', status=404)