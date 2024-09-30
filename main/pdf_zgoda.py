import os
from django.conf import settings
from .models import zgoda_bat
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Clients

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from PyPDF2 import PdfReader, PdfWriter



def zgoda(existing_pdf_path, client_id):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)

    data010 = zgoda_bat.objects.get(client_id=client_id)

    first_photo_width = 400
    first_photo_height = 500
    first_photo_x = 120
    first_photo_y = 220

    if data010.photo_zgodu:
        c.drawImage(os.path.join(settings.MEDIA_ROOT, str(data010.photo_zgodu)), first_photo_x, first_photo_y,
                    width=first_photo_width, height=first_photo_height)

    c.save()
    packet.seek(0)

    overlay_pdf = PdfReader(packet)

    existing_pdf = PdfReader(existing_pdf_path)

    output = PdfWriter()

    for page_num in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[page_num]
        page.merge_page(overlay_pdf.pages[0])
        output.add_page(page)

    return output

# Створення pdf документа зі всіма документами

def generate_zgoda(request, id):
    el = get_object_or_404(Clients, id=id)
    el2 = zgoda_bat.objects.get(client_id=el.id)

    existing_pdf_path = "main/pdf/zgoda_bat.pdf"

    new_pdf = zgoda(existing_pdf_path, el.id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Згода.pdf"'

    output_stream = io.BytesIO()
    new_pdf.write(output_stream)
    response.write(output_stream.getvalue())

    return response


