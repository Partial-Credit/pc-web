from django.contrib import admin

# Register your models here.
from .models import Song
from .models import Album
admin.site.register(Album)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	filter_horizontal = ('arranger', 'soloist', 'vocal_percussion')