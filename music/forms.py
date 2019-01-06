from django import forms
from django.contrib import admin
from . import models
from django.contrib.admin.widgets import FilteredSelectMultiple
import sys
sys.path.append(sys.path[0] + "\\users")
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from users.models import Member

class SongForm(forms.ModelForm):
	arranger = forms.ModelMultipleChoiceField(queryset=Member.objects.order_by('last_name').all(), widget= forms.CheckboxSelectMultiple(), required=True)
	soloist = forms.ModelMultipleChoiceField(queryset=Member.objects.order_by('last_name').all(), widget=forms.CheckboxSelectMultiple(), required=False)
	vocal_percussion= forms.ModelMultipleChoiceField(queryset=Member.objects.order_by('last_name').all(), widget=forms.CheckboxSelectMultiple(), required=False)
	class Meta:
		model = models.Song
		fields = '__all__'
		widgets = {
			'arranger': forms.CheckboxSelectMultiple(),
			'soloist': forms.CheckboxSelectMultiple(),
			'vocal_percussion': forms.CheckboxSelectMultiple(),
		}

class AlbumForm(forms.ModelForm):
	songs = forms.ModelMultipleChoiceField(queryset=models.Song.objects.order_by('title').all(), widget=forms.CheckboxSelectMultiple())
	class Meta:
		model = models.Album
		fields = '__all__'

