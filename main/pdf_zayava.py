import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Clients,Sing_Clients
from reportlab.lib.enums import TA_LEFT
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
def creat(existing_pdf, id):
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

    draw_paragraph(c, f"{data8.name2}", 425, 705, 100, 15)
    draw_paragraph(c, f"{data8.fname2}", 510, 705, 100, 15)
    draw_paragraph(c, f"{data8.soname2}", 350, 705, 100, 15)
    draw_paragraph(c, f"{data8.date}", 315, 685, 140, 15)
    draw_paragraph(c, f"{data8.lang}", 280, 385, 240, 15)
    draw_paragraph(c, f"{data8.document}", 430, 605, 240, 15)
    draw_paragraph(c, f"{data8.num}", 375, 590, 240, 15)
    draw_paragraph(c, f"{data8.born}", 315, 655, 240, 15)

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


def Download_PDF(request, id):
    el = Clients.objects.get(id=id)
    el2 = get_object_or_404(Sing_Clients, client_id=el.id)
    # Path to the existing PDF file
    existing_pdf_path = "main/pdf/zayava.pdf"

    with open(existing_pdf_path, "rb") as f:
        existing_pdf_bytes = f.read()
    existing_pdf = PdfReader(io.BytesIO(existing_pdf_bytes))

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Заява.pdf"'

    new_pdf = creat(existing_pdf, el.id)

    output_stream = io.BytesIO()
    new_pdf.write(output_stream)
    response.write(output_stream.getvalue())
    output_stream.close()

    return response