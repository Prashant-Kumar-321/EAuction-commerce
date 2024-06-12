from django.db import models 

class Comment(models.Model): 
	comment = models.TextField()
	comment_date = models.DateField(auto_now_add=True)

	def __str__(self): 
		return f"Comment = {self.comment} Time: {self.comment_date} endTime: {self.end_date}"