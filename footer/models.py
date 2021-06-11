from django.db import models

# Create your models here.

class endfooter(models.Model):
	"""docstring for endfooter"""

	copyright = models.CharField(max_length=50, blank=False)
	designed  = models.CharField(max_length=50, blank=False)
	facebook  = models.CharField(max_length=50, blank=False)
	teitter   = models.CharField(max_length=50, blank=False)
	linkden	  = models.CharField(max_length=50, blank=False)
	instragram= models.CharField(max_length=50, blank=False)

	
	def __str__(self):
		return self.copyright