from django.db import models

# Create your models here.

class contact(models.Model):
	"""docstring for contact_query"""
	name 		= models.CharField(max_length=50, blank=False)
	email 		= models.TextField(max_length=30, blank=False)
	subject 	= models.TextField(max_length=80, blank=False)
	description = models.TextField(max_length=900, blank=False)
	
	def __str__(self):
		return self.subject



class information(models.Model):
	"""docstring for information"""
	location 	= models.CharField(max_length=80, blank=False)
	email 		= models.TextField(max_length=30, blank=False)
	email2 		= models.TextField(max_length=30, blank=False)
	call 		=  models.CharField(max_length=15, blank=False)
	call2 		=  models.CharField(max_length=15, blank=False)

	def __str__(self):
		return self.location
	