from django.db import models 
from .user import User 
from .categories import Category 

class Listing(models.Model): 
	title = models.CharField(blank=False, max_length=100) 
	description = models.TextField()
	org_bid = models.PositiveBigIntegerField() 
	running_bid = models.PositiveBigIntegerField() 
	final_bid = models.PositiveBigIntegerField(null=True, blank=True) # price of the listing when it will be inactive 
	is_active = models.BooleanField(default=True) 
	winner= models.ForeignKey(User, null = True, blank=True, related_name="winner", on_delete=models.PROTECT) 
	watch_list = models.ManyToManyField(User, blank=True, related_name="watch_list")  # using this related name i can get all the listings that is in the watch list of an user 
	ctg = models.ForeignKey(Category, related_name='category', on_delete=models.PROTECT)
	owner = models.ForeignKey(User, related_name='owner', on_delete=models.PROTECT, blank=False) 
	image = models.ImageField(null=True, blank=True, upload_to="images/")

""" 
	Problem To Do.. 
	1. 
	What if owner of listings close biding and 
    Whe have two user that have bid the same which is final price 
    of the listing. 

	2. 
	owner delete his account 
	listings 
	1. closed 
	2. running -> Will never end


""" 
""" 
	Temporary solution 
	
	P2. 
	For simplicity 
	leave the listings

"""


