import os
from django.conf import settings
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Clients, Anketa
from reportlab.lib.enums import TA_LEFT
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
def create_pdf2(existing_pdf, id):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    width, height = letter
    el = get_object_or_404(Clients, id=id)
    data1 = Anketa.objects.get(client_id=el.id)

    pdfmetrics.registerFont(TTFont('DejaVuSans', 'main/front/DejaVuSans.ttf'))
    styles = getSampleStyleSheet()
    style = styles['Normal']
    style.fontName = 'DejaVuSans'
    style.alignment = TA_LEFT

    def draw_paragraph(c, text, x, y, max_width, max_height):
        p = Paragraph(text, style)
        p.wrapOn(c, max_width, max_height)
        p.drawOn(c, x, y - p.height)

    image_path = os.path.join(settings.MEDIA_ROOT, str(data1.photo))
    c.drawImage(image_path, 470, 649, width=35 * 72 / 25.4, height=45 * 72 / 25.4)

    draw_paragraph(c, f"{data1.nsf}", 338, 565, 240, 15)
    draw_paragraph(c, f"{data1.ed_nsf}", 338, 535, 240, 15)
    draw_paragraph(c, f"{data1.born}", 338, 486, 240, 15)
    draw_paragraph(c, f"{data1.place}", 338, 440, 240, 15)
    draw_paragraph(c, f"{data1.place_register}", 338, 390, 240, 15)
    draw_paragraph(c, f"{data1.place_live}", 338, 350, 240, 15)
    draw_paragraph(c, f"{data1.cityzen}", 338, 320, 240, 15)
    draw_paragraph(c, f"{data1.edit_cit}", 338, 230, 240, 15)
    draw_paragraph(c, f"{data1.pasport}", 338, 170, 240, 15)
    draw_paragraph(c, f"{data1.pasport_c}", 338, 120, 240, 15)

    c.showPage()

    draw_paragraph(c, f"{data1.en_doc}", 338, 715, 240, 15)
    draw_paragraph(c, f"{data1.education}", 338, 655, 240, 15)
    draw_paragraph(c, f"{data1.duplom}", 338, 585, 240, 15)
    draw_paragraph(c, f"{data1.len}", 338, 535, 240, 15)
    draw_paragraph(c, f"{data1.social_med}", 338, 478, 240, 15)
    draw_paragraph(c, f"{data1.tz}", 338, 430, 240, 15)
    draw_paragraph(c, f"{data1.zbroi}", 338, 358, 240, 15)
    draw_paragraph(c, f"{data1.crimanal}", 338, 280, 240, 15)
    draw_paragraph(c, f"{data1.teritory}", 338, 200, 240, 15)
    c.showPage()

    draw_paragraph(c, f"{data1.rf}", 338, 714, 240, 15)
    draw_paragraph(c, f"{data1.stupin}", 87, 534, 150, 15)
    draw_paragraph(c, f"{data1.name1}", 150, 534, 80, 15)
    draw_paragraph(c, f"{data1.born1}", 310, 534, 80, 15)
    draw_paragraph(c, f"{data1.work1}", 392, 534, 90, 15)
    draw_paragraph(c, f"{data1.adress}", 494, 534, 100, 5)

    draw_paragraph(c, f"{data1.stupin2}", 87, 474, 240, 15)
    draw_paragraph(c, f"{data1.name2}", 150, 474, 80, 15)
    draw_paragraph(c, f"{data1.born2}", 310, 474, 80, 15)
    draw_paragraph(c, f"{data1.work2}", 392, 474, 90, 15)
    draw_paragraph(c, f"{data1.adress2}", 494, 474, 100, 5)

    draw_paragraph(c, f"{data1.stupin3}", 87, 413, 240, 15)
    draw_paragraph(c, f"{data1.name3}", 150, 413, 80, 15)
    draw_paragraph(c, f"{data1.born3}", 310, 413, 80, 15)
    draw_paragraph(c, f"{data1.work3}", 392, 413, 90, 15)
    draw_paragraph(c, f"{data1.adress3}", 494, 413, 100, 5)

    draw_paragraph(c, f"{data1.stupin4}", 87, 347, 240, 15)
    draw_paragraph(c, f"{data1.name4}", 150, 347, 80, 15)
    draw_paragraph(c, f"{data1.born4}", 310, 347, 80, 15)
    draw_paragraph(c, f"{data1.work4}", 392, 347, 90, 15)
    draw_paragraph(c, f"{data1.adress4}", 494, 347, 100, 5)

    draw_paragraph(c, f"{data1.stupin5}", 87, 285, 240, 15)
    draw_paragraph(c, f"{data1.name5}", 150, 285, 80, 15)
    draw_paragraph(c, f"{data1.born5}", 310, 285, 80, 15)
    draw_paragraph(c, f"{data1.work5}", 392, 285, 90, 15)
    draw_paragraph(c, f"{data1.adress5}", 494, 285, 100, 5)

    draw_paragraph(c, f"{data1.stupin6}", 87, 225, 240, 15)
    draw_paragraph(c, f"{data1.name6}", 150, 225, 80, 15)
    draw_paragraph(c, f"{data1.born6}", 310, 225, 80, 15)
    draw_paragraph(c, f"{data1.work6}", 392, 225, 90, 15)
    draw_paragraph(c, f"{data1.adress6}", 494, 225, 100, 5)

    draw_paragraph(c, f"{data1.stupin7}", 87, 160, 240, 15)
    draw_paragraph(c, f"{data1.name7}", 150, 160, 80, 15)
    draw_paragraph(c, f"{data1.born7}", 310, 160, 80, 15)
    draw_paragraph(c, f"{data1.work7}", 392, 160, 90, 15)
    draw_paragraph(c, f"{data1.adress7}", 494, 160, 100, 5)
    c.showPage()

    draw_paragraph(c, f"{data1.stupin8}", 87, 730, 240, 15)
    draw_paragraph(c, f"{data1.name8}", 150, 730, 80, 15)
    draw_paragraph(c, f"{data1.born8}", 310, 730, 80, 15)
    draw_paragraph(c, f"{data1.work8}", 392, 730, 90, 15)
    draw_paragraph(c, f"{data1.adress8}", 494, 730, 100, 5)

    draw_paragraph(c, f"{data1.vstup}", 87, 494, 50, 15)
    draw_paragraph(c, f"{data1.zvil}", 165, 494, 50, 15)
    draw_paragraph(c, f"{data1.posada}", 240, 494, 240, 15)
    draw_paragraph(c, f"{data1.location}", 455, 494, 150, 15)

    draw_paragraph(c, f"{data1.vstup1}", 87, 445, 50, 15)
    draw_paragraph(c, f"{data1.zvil1}", 165, 445, 50, 15)
    draw_paragraph(c, f"{data1.posada1}", 240, 445, 240, 15)
    draw_paragraph(c, f"{data1.location1}", 455, 445, 150, 15)

    draw_paragraph(c, f"{data1.vstup2}", 87, 390, 50, 15)
    draw_paragraph(c, f"{data1.zvil2}", 165, 390, 50, 15)
    draw_paragraph(c, f"{data1.posada2}", 240, 390, 240, 15)
    draw_paragraph(c, f"{data1.location2}", 455, 390, 150, 15)

    draw_paragraph(c, f"{data1.vstup4}", 87, 165, 50, 15)
    draw_paragraph(c, f"{data1.zvil4}", 162, 165, 50, 15)
    draw_paragraph(c, f"{data1.posada4}", 236, 165, 240, 15)
    draw_paragraph(c, f"{data1.location4}", 455, 165, 150, 15)

    draw_paragraph(c, f"{data1.vstup5}", 87, 110, 50, 15)
    draw_paragraph(c, f"{data1.zvil5}", 162, 110, 50, 15)
    draw_paragraph(c, f"{data1.posada5}", 236, 110, 240, 15)
    draw_paragraph(c, f"{data1.location5}", 455, 110, 150, 15)
    c.showPage()

    draw_paragraph(c, f"{data1.seria_num}", 167, 668, 360, 15)
    draw_paragraph(c, f"{data1.kum}", 205, 652, 350, 15)
    draw_paragraph(c, f"{data1.kontact_sl}", 156, 604, 150, 15)
    draw_paragraph(c, f"{data1.kontact_os}", 365, 604, 150, 15)
    draw_paragraph(c, f"{data1.kontact_fa}", 130, 588, 150, 15)
    draw_paragraph(c, f"{data1.kontact_ma}", 345, 588, 150, 15)
    draw_paragraph(c, f"{data1.data22}", 100, 555, 120, 15)
    c.showPage()

    c.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)

    output = PdfWriter()
    for pageNum in range(len(existing_pdf.pages)):
        # Отримання сторінки з існуючого PDF
        existing_page = existing_pdf.pages[pageNum]

        if pageNum == 0:
            # Об'єднання першої сторінки з даними
            new_page = new_pdf.pages[0]
            existing_page.merge_page(new_page)
        elif pageNum == 1:
            # Об'єднання другої сторінки з даними
            new_page = new_pdf.pages[1]
            existing_page.merge_page(new_page)
        elif pageNum == 2:
            # Об'єднання 3 сторінки з даними
            new_page = new_pdf.pages[2]
            existing_page.merge_page(new_page)
        elif pageNum == 3:
            # Об'єднання 4 сторінки з даними
            new_page = new_pdf.pages[3]
            existing_page.merge_page(new_page)
        elif pageNum == 4:
            # Об'єднання 4 сторінки з даними
            new_page = new_pdf.pages[4]
            existing_page.merge_page(new_page)
        elif pageNum == 5:
            # Об'єднання 4 сторінки з даними
            new_page = new_pdf.pages[5]
            existing_page.merge_page(new_page)

        # Додавання об'єднаної сторінки до вихідного PDF
        output.add_page(existing_page)

    return output


def generate_pdf(request, id):
    el = Clients.objects.get(id=id)
    el2 = get_object_or_404(Anketa, client_id=el.id)
    existing_pdf_path = "main/pdf/anketa-6.pdf"

    existing_pdf = PdfReader(existing_pdf_path)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Анкета.pdf"'

    new_pdf = create_pdf2(existing_pdf, el.id)
    output_stream = io.BytesIO()
    new_pdf.write(output_stream)
    response.write(output_stream.getvalue())
    output_stream.close()

    return response