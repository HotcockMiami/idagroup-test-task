from os import path
from urllib.request import urlopen
from django import forms
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from .models import Picture

class PictureForm(forms.ModelForm):
    image_url = forms.URLField(required=False, label='Ссылка')

    def clean(self):
        all_data = self.cleaned_data # Берём данные
        url = all_data['image_url']
        image_orig = all_data['image_orig']

        if (image_orig and url) or (not image_orig and not url): # Проверяем на неправильный ввод
            raise forms.ValidationError('One of two fields is required :)')

        if not image_orig and url: # Если фотография загружается по URL, то "забираем" её с ресурса
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(url).read())
            all_data['image_orig'] = File(img_temp, name=path.basename(url))
            all_data['image_resized'] = File(img_temp, name=path.basename(url))
            all_data['image_url'] = url
            print(all_data)
            img_temp.flush()

        else:
            all_data['image_resized'] = all_data['image_orig']

        return all_data

    class Meta:
        model = Picture
        fields = ('image_orig', 'image_url', 'image_resized')
        labels = {
            'image_orig': 'Файл',
        }
        widgets = {
            'image_resized': forms.HiddenInput()
        }

class ResizeForm(forms.Form): # Формы для высоты и ширины изображения с минимальным лимитом
    height = forms.IntegerField(required=False, min_value=1)
    width = forms.IntegerField(required=False, min_value=1)
