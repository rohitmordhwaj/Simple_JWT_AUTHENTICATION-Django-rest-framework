from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):

	first_name   =  models.CharField(max_length = 200 , default ="first_name")
	last_name    =  models.CharField(max_length = 200 , default="last_name")
	username     =  models.CharField(max_length = 200, default="username")



	def __str__(self):
		return self.username


class Post(models.Model):
	text 		= models.CharField(max_length = 20000)
	created_by	= models.ForeignKey(Author ,on_delete=models.CASCADE)
	created_at  = models.DateTimeField(auto_now_add=True) 
	updated_at = models.DateTimeField(auto_now=True)  


	
		

	
