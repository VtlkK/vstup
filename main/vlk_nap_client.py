from django.http import HttpResponse, Http404
from .models import vlk_napr, Clients
from django.views.decorators.cache import never_cache

@never_cache
def download_pdf(request, id):
    try:
        el = vlk_napr.objects.get(id=id)
        if not el.pdf:
            raise Http404("PDF файл не знайдено.")
        response = HttpResponse(el.pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{el.pdf.name}"'
        return response
    except vlk_napr.DoesNotExist:
        raise Http404("Направлення не знайдено.")