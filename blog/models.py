from django.db import models

# Create your models here.

class blog(models.Model):
	"""docstring for contact_query"""
	title 		= models.CharField(max_length=200, blank=False)
	datetime 	= models.DateTimeField(blank=True)
	description = models.TextField(max_length=2000, blank=False)	

	
	def __str__(self):
		return self.title
