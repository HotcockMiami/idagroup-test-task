import os
from io import BytesIO
from PIL import Image, ImageOps
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.files.base import ContentFile
from .forms import PictureForm, ResizeForm
from .models import Picture

def upload(request): # Загружаем данные из формы и перенапрявляем на фото
    form = PictureForm
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return HttpResponseRedirect('resize/%s' % post.id)

    else:
        form = PictureForm()

    return render(request, 'upload.html', {'form': form})

def resize(request, pk):
    form = ResizeForm
    instance = get_object_or_404(Picture, id=pk)
    if request.method == "POST":
        form = ResizeForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data                     # Берём высоту и ширину из формы
            w = post['width']
            h = post['height']
            img = Image.open(instance.image_orig)        # Открываем изображение PIL'ом

            img_ratio = float(img.size[0]) / img.size[1] # Расчитываем aspect ratio
            if w is None:                                # Используем его при необходимости
                w = h * img_ratio
            elif h is None:
                h = w / img_ratio
            img = img.resize ((int(w),int(h)))           # Задаем высоту и ширину

            f = BytesIO()
            img.save(f, format='png')
            os.remove(instance.image_resized.path)
            instance.image_resized.save(os.path.basename(instance.image_resized.name),
                                        ContentFile(f.getvalue())) # PIL -> ImageField
            f.close()
            return HttpResponseRedirect('/images/resize/%s' % instance.id)
    else:
        form = ResizeForm()
    return render(request, 'resize.html', {'form': form, 'inst' : instance})

def index(request):
    model = Picture.objects.all()
    return render(request, 'index.html', {'pics' : model})
