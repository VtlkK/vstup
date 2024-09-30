from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import io
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Clients, Sing_Clients
from PyPDF2 import PdfReader, PdfWriter
from django.views.decorators.cache import never_cache


def zgoda_p(existing_pdf, id):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    width, height = letter
    el = get_object_or_404(Clients, id=id)
    data79 = Sing_Clients.objects.get(client_id=el.id)

    pdfmetrics.registerFont(TTFont('DejaVuSans', 'main/front/DejaVuSans.ttf'))
    styles = getSampleStyleSheet()
    style = styles['Normal']
    style.fontName = 'DejaVuSans'
    style.alignment = TA_LEFT

    def draw_paragraph(c, text, x, y, max_width, max_height):
        p = Paragraph(text, style)
        p.wrapOn(c, max_width, max_height)
        p.drawOn(c, x, y - p.height)
    draw_paragraph(c, f"{data79.fname}", 300, 735, 240, 15)
    draw_paragraph(c, f"{data79.name}", 230, 735, 240, 15)
    draw_paragraph(c, f"{data79.soname}", 140, 735, 240, 15)
    draw_paragraph(c, f"{data79.date}", 140, 710, 240, 15)
    draw_paragraph(c, f"{data79.document}", 140, 693, 240, 15)

    draw_paragraph(c, f"{data79.fname}", 300, 455, 240, 15)
    draw_paragraph(c, f"{data79.name}", 230, 455, 240, 15)
    draw_paragraph(c, f"{data79.soname}", 140, 455, 240, 15)


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

        output.add_page(existing_page)

    return output

#Створення pdf документи зі всіма документами
def download_zgoda_p(request, id):
    el = get_object_or_404(Clients, id=id)
    el2 = Sing_Clients.objects.get(client_id=el.id)
    existing_pdf_path = "main/pdf/zgoda_p1.pdf"
    existing_pdf = PdfReader(existing_pdf_path)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="edited_{el2.id}.pdf"'
    new_pdf = zgoda_p(existing_pdf, el.id)
    output_stream = io.BytesIO()
    new_pdf.write(output_stream)
    response.write(output_stream.getvalue())
    output_stream.close()
    return response

