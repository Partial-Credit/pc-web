from django.db import models
from django import forms
import sys
sys.path.append(sys.path[0] + "\\users")
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Member
# Create your models here.
class Song(models.Model):
	title = models.CharField(max_length=100)
	opb = models.CharField(max_length=100)
	arranger = models.ManyToManyField(Member, related_name="arranger", symmetrical=False) 
	soloist =  models.ManyToManyField(Member, related_name="soloist", blank=True, symmetrical=False) 
	vocal_percussion = models.ManyToManyField(Member, related_name="vocal_percussion", blank=True, symmetrical=False) 

	def __str__(self):
		return self.title

class Album(models.Model):
	cover = models.ImageField(blank=True, default='default.png')
	title = models.CharField(max_length=100)
	release_year = models.PositiveSmallIntegerField (
        validators=[ MinValueValidator(2000) ],
        blank=True,
        null=True,
        help_text = "Please use the following format: <em>YYYY</em>."
    )
	songs = models.ManyToManyField(Song, related_name="songs", blank=True, symmetrical=False)  

	def __str__(self):
		return self.title

class CreateSong(forms.ModelForm):
	class Meta:
		model = Song
		fields = ['title', 'opb', 'arranger', 'soloist', 'vocal_percussion']
