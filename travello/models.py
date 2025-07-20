from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from sorl.thumbnail import ImageField
 
 

# Create your models here.
class Destination(models.Model):
	 
	name= models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	desc= models.TextField()
	price= models.IntegerField()
	offer= models.BooleanField(default=False)

	def __str__(self):
		return self.name


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    destinations = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='wish_destination', blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '{} // {}'.format(self.user, self.destinations.name)

class Checkorder(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    postal_code = models.IntegerField()
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return sum([ li.cost() for li in self.allorder_set.all() ] )        





class Allorder(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    checkorder = models.ForeignKey(Checkorder, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    destinations = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='Allorder_destination')
    order_date = models.DateTimeField(auto_now_add=True)
    

    #모델 인스턴스를 아이디 값 내림차순 정렬
    class Meta:
        ordering = ('-id',)

    def __str__(self):
       return '{} by {}'.format(self.destinations.name, self.user)

    def cost(self):
        return self.quantity * self.destinations.price 
    

 