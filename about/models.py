from django.db import models

# Create your models here.

class about_mod(models.Model):
	title 		= models.CharField(max_length=80, blank=False)
	sub_title 	= models.TextField(max_length=150, blank=False)
	description = models.TextField(max_length=1000, blank=False)
	
	def __str__(self):
		return self.title

# class our_team(models.Model):
# 	title 		= models.CharField(max_length=150, blank=False)
# 	sub_title 	= models.TextField(max_length=500, blank=False)
# 	image 		= models.
# 	facebook  	= models.CharField(max_length=50, blank=False)
# 	teitter   	= models.CharField(max_length=50, blank=False)
# 	linkden	  	= models.CharField(max_length=50, blank=False)
# 	instragram	= models.CharField(max_length=50, blank=False)
	
# 	def __str__(self):
# 		return self.title
