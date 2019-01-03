from PIL import Image
from django import forms
from django.core.files import File
from .models import CoverPhoto

class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
    	model = CoverPhoto
    	fields = ('thumb', 'title', 'x', 'y', 'width', 'height')

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        print("x: {:f}, y: {:f}, width: {:f}, height: {:f}".format(x,y,w,h))
        image = Image.open(photo.thumb)
        cropped_image = image.crop((x, y, w+x, h+y))
        cropped_image.save(photo.thumb.path)
		
        return photo