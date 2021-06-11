from django.db import models

# Create your models here.

class about_mod(models.Model):
	title 		= models.CharField(max_length=80, blank=False)
	sub_title 	= models.TextField(max_length=150, blank=False)
	description = models.TextField(max_length=1000, blank=False)
	def __str__(self):
		return self.title
