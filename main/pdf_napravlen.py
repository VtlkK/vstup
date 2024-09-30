import io
import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from vstupProject import settings
from .models import Clients, Sing_Clients, Anketa
from reportlab.lib.enums import TA_LEFT
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
def creat_napravlen(existing_pdf, id):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    width, height = letter
    el = Clients.objects.get(id=id)
    data8 = Sing_Clients.objects.get(client_id=el.id)

    pdfmetrics.registerFont(TTFont('DejaVuSans', 'main/front/DejaVuSans.ttf'))
    styles = getSampleStyleSheet()
    style = styles['Normal']
    style.fontName = 'DejaVuSans'
    style.alignment = TA_LEFT

    def draw_paragraph(c, text, x, y, max_width, max_height):
        p = Paragraph(text, style)
        p.wrapOn(c, max_width, max_height)
        p.drawOn(c, x, y - p.height)

    if data8.sex == 'Чол.':
        draw_paragraph(c, 'громадянина', 215, 686, 100, 15)
    else:
        draw_paragraph(c, 'громадянки', 215, 686, 100, 15)
    draw_paragraph(c, f"{data8.name2}", 385, 686, 100, 15)
    draw_paragraph(c, f"{data8.fname2}", 475, 686, 100, 15)
    draw_paragraph(c, f"{data8.soname2}", 297, 686, 100, 15)
    draw_paragraph(c, f"{data8.date}", 75, 667, 140, 15)
    c.showPage()

    draw_paragraph(c, f"{data8.name}", 325, 639, 100, 15)
    draw_paragraph(c, f"{data8.fname}", 445, 639, 100, 15)
    draw_paragraph(c, f"{data8.soname}", 220, 639, 100, 15)
    draw_paragraph(c, f"{data8.date}", 170, 605, 140, 15)
    draw_paragraph(c, f"{data8.born}", 230, 587, 450, 15)
    try:
        data1 = Anketa.objects.get(client_id=el.id)
    except Anketa.DoesNotExist:
        data1 = None
    image_path = os.path.join(settings.MEDIA_ROOT, str(data1.photo))
    c.drawImage(image_path, 70, 701, width=3.5 * 52 / 2.54, height=4.5 * 52 / 2.54)
    c.showPage()
    c.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)

    output = PdfWriter()
    for pageNum in range(len(existing_pdf.pages)):
        existing_page = existing_pdf.pages[pageNum]

        if pageNum == 0:
            new_page = new_pdf.pages[0]
            existing_page.merge_page(new_page)
        elif pageNum == 1:
            new_page = new_pdf.pages[1]
            existing_page.merge_page(new_page)

        output.add_page(existing_page)

    return output


def download_PDF(request, id):
    el = Clients.objects.get(id=id)
    el2 = get_object_or_404(Sing_Clients, client_id=el.id)
    existing_pdf_path = "main/pdf/napr_vlk.pdf"

    with open(existing_pdf_path, "rb") as f:
        existing_pdf_bytes = f.read()
    existing_pdf = PdfReader(io.BytesIO(existing_pdf_bytes))

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="vlk_{el2.id}.pdf"'

    new_pdf = creat_napravlen(existing_pdf, el.id)

    output_stream = io.BytesIO()
    new_pdf.write(output_stream)
    response.write(output_stream.getvalue())
    output_stream.close()

    return response