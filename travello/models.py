from django.db import models
from django.contrib.auth.models import User  
 

# Create your models here.
class Destination(models.Model):
	 
	name= models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	desc= models.TextField()
	price= models.IntegerField()
	offer= models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Item(models.Model):
	 
	title= models.CharField(max_length=100)
	price= models.FloatField()
	offer= models.BooleanField(default=False)

	def __str__(self):
		return self.title

class OrderItem(models.Model):
	 
	item= models.ForeignKey(Item, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Order(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	items= models.ManyToManyField(OrderItem)
	start_date=models.DateTimeField()
     
	   


	#def __str__(self):
		#return self.user.username 