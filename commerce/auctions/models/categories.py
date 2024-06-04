from django.db import models 

class Category(models.Model): 
	ctg = models.CharField(max_length = 100, blank=False) 

	def __str__(self): 
		return f"{self.ctg}"

""" 	
	This relation will hold all category available in the Auction of listings 
"""