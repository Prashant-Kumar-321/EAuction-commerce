from django.db import models 

class Listing(models.Model): 
	title = models.CharField(blank=False, max_length=100) 
	description = models.TextFeild()
	image = models.ImageField()
	pass 