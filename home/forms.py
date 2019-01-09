from PIL import Image
from django import forms
from django.core.files import File
from .models import CoverPhoto, Article
import sys

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'thumb']

class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
    	model = CoverPhoto
    	fields = ('title', 'order', 'image', 'title', 'x', 'y', 'width', 'height')

    def save(self):
        photo = super(PhotoForm, self).save()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x == 0 and y == 0 and w == 0 and h == 0:
            return photo 

        image = Image.open(photo.image)
        cropped_image = image.crop((x, y, w+x, h+y))
        
        if photo.thumb.path[-11:] == 'default.png':
            img_index = photo.image.path.rfind("\\")
            end_index = photo.image.path.rfind('.')
            img_name = photo.image.path[img_index + 1: end_index]
            file_extension = photo.image.path[end_index:]
            
            cropped_name = img_name + "_copy" + file_extension
            path = sys.path[0] + "\\assets\\" + cropped_name
            
            cropped_image.save(path)
            photo.thumb.save(cropped_name, File(open(path, 'rb')))
        
        else:
            path = photo.thumb.path
            cropped_image.save(path)
            photo.save()

        return photo