import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Clients, corup
from reportlab.lib.enums import TA_LEFT
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
def cor(existing_pdf, id):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    width, height = letter
    el = get_object_or_404(Clients, id=id)
    data0 = corup.objects.get(client_id=el.id)
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'main/front/DejaVuSans.ttf'))
    styles = getSampleStyleSheet()
    style = styles['Normal']
    style.fontName = 'DejaVuSans'
    style.alignment = TA_LEFT

    def draw_paragraph(c, text, x, y, max_width, max_height):
        p = Paragraph(text, style)
        p.wrapOn(c, max_width, max_height)
        p.drawOn(c, x, y - p.height)
    draw_paragraph(c, f"{data0.f22}", 90, 630, 240, 15)
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

#Створення pdf заяви на відсутність родичів в ДПСУ
def generate_cor(request, id):
    el = get_object_or_404(Clients, id=id)
    el2 = corup.objects.get(client_id=el.id)
    existing_pdf_path = "main/pdf/corup.pdf"
    existing_pdf = PdfReader(existing_pdf_path)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Наявність_родичів.pdf"'
    new_pdf = cor(existing_pdf, el.id)
    output_stream = io.BytesIO()
    new_pdf.write(output_stream)
    response.write(output_stream.getvalue())
    output_stream.close()
    return response
