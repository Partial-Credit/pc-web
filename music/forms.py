from django import forms
from django.contrib import admin
from . import models
from django.contrib.admin.widgets import FilteredSelectMultiple
import sys
sys.path.append(sys.path[0] + "\\users")
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from users.models import Member

class CreateSong(forms.Form):
	title = forms.CharField(max_length=100)
	opb = forms.CharField(max_length=100)
	arranger = forms.ModelMultipleChoiceField(queryset=Member.objects.order_by('last_name').all(), widget= forms.CheckboxSelectMultiple())
	soloist = forms.ModelMultipleChoiceField(queryset=Member.objects.order_by('last_name').all(), widget=forms.CheckboxSelectMultiple())
	vocal_percussion= forms.ModelMultipleChoiceField(queryset=Member.objects.order_by('last_name').all(), widget=forms.CheckboxSelectMultiple())

class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = '__all__'
        widgets = {
            'arranger': forms.CheckboxSelectMultiple(),
            'soloist': forms.CheckboxSelectMultiple(),
			'vocal_percussion': forms.CheckboxSelectMultiple(),

        }


