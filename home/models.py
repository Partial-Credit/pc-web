from django.db import models
from django.contrib.auth.models import User
import importlib
from django.conf import settings
# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
	#add author later
	
	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:100] + '...'

	def save(self, *args, **kwargs):
		super(Article, self).save(*args, **kwargs)
		slug = list(self.title)
		for i in range(len(self.title)):
			if not self.title[i].isalpha() and not self.title[i].isdigit() and \
				self.title[i] != "-" and self.title[i] != "_":
				slug[i] = ""
		slug = ''.join(slug)
		print(slug)
		self.slug = slug.replace(' ','-').lower()
		kwargs['force_insert'] = False # create() uses this, which causes error.
		super(Article, self).save(*args, **kwargs)

class CoverPhoto(models.Model):
	title = models.CharField(max_length=100)
	order = models.PositiveSmallIntegerField(default = 0, blank = True)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return self.title	

	def save(self, *args, **kwargs):
		add = not self.pk
		super(CoverPhoto, self).save(*args, **kwargs)
		if add:
			self.order = int(self.pk)
			kwargs['force_insert'] = False # create() uses this, which causes error.
			super(CoverPhoto, self).save(*args, **kwargs)