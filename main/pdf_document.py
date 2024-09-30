import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Clients, documents
from reportlab.lib.enums import TA_LEFT
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from PyPDF2 import PdfReader, PdfWriter
import os
from django.conf import settings


def documents33(existing_pdf, id):
    # Створення canvas для редагування
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    width, height = letter
    el = get_object_or_404(Clients, id=id)
    # Зчитування даних з бази даних
    data78 = documents.objects.get(client_id=el.id)

    # Розміри і позиції перших двох фотографій
    first_photo_width = 320
    first_photo_height = 240
    first_photo_x = 80
    first_photo_y = 450

    second_photo_width = 320
    second_photo_height = 240
    second_photo_x = 80
    second_photo_y = 100

    other_photo_width = 490
    other_photo_height = 570
    other_photo_x = 40
    other_photo_y = 200

    # Додавання перших двох фотографій
    if data78.id_card:
        c.drawImage(os.path.join(settings.MEDIA_ROOT, str(data78.id_card)), first_photo_x, first_photo_y,
                    width=first_photo_width, height=first_photo_height)
    if data78.id_card2:
        c.drawImage(os.path.join(settings.MEDIA_ROOT, str(data78.id_card2)), second_photo_x, second_photo_y,
                    width=second_photo_width, height=second_photo_height)

    c.showPage()


    other_photos = [
        data78.plat_doc,
        data78.psix_doc,
        data78.photo_doc,
        data78.cruminal_doc,
        data78.location_doc,
        data78.born_doc,
        data78.spec_doc
    ]

    for photo in other_photos:
        if photo:
            c.drawImage(os.path.join(settings.MEDIA_ROOT, str(photo)), other_photo_x, other_photo_y,
                        width=other_photo_width, height=other_photo_height)
            c.showPage()

    c.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)

    output = PdfWriter()
    for pageNum in range(len(existing_pdf.pages)):
        # Отримання сторінки з існуючого PDF
        existing_page = existing_pdf.pages[pageNum]

        if pageNum < len(new_pdf.pages):
            new_page = new_pdf.pages[pageNum]
            existing_page.merge_page(new_page)

        output.add_page(existing_page)

    return output

#Створення pdf документи зі всіма документами
def generate_doc(request, id):
    el = get_object_or_404(Clients, id=id)
    el2 = documents.objects.get(client_id=el.id)
    existing_pdf_path = "main/pdf/all_doc2.pdf"
    existing_pdf = PdfReader(existing_pdf_path)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Документи.pdf"'
    new_pdf = documents33(existing_pdf, el.id)
    output_stream = io.BytesIO()
    new_pdf.write(output_stream)
    response.write(output_stream.getvalue())
    output_stream.close()
    return response