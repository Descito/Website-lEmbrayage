from django.db import models

# Create your models here.
class Prjt(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='yage/images/')
	url = models.URLField(blank=True)