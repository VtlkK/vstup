from django.shortcuts import redirect, render

from .models import Moder_napr, Clients

from django.views.decorators.cache import never_cache

@never_cache
def moder_vlknapr_vid(request, id):
    el = Clients.objects.get(id=id)

    if request.method == 'POST':
        images = request.FILES.getlist('napr_img')  # Отримання всіх файлів з форми

        # Перевірка чи є файли
        if images:
            for image in images:
                Moder_napr.objects.create(client=el, napr_img=image)

            return redirect('cabinet', el.id)

    return render(request, 'main/cabinet.html', {'el': el})