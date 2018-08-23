from django.db import models
import sys
sys.path.append(sys.path[0] + "\\users")
from users.models import Member
# Create your models here.
class Song(models.Model):
	title = models.CharField(max_length=100)
	opb = models.CharField(max_length=100)
	arranger = models.ManyToManyField(Member, related_name="arranger") 
	soloist =  models.ManyToManyField(Member, related_name="soloist") 
	vocal_percussion = models.ManyToManyField(Member, related_name="vocal_percussion") 

	def __str__(self):
		return self.title
