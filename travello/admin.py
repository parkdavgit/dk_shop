from django.contrib import admin
from .models import Destination, Item, OrderItem, Order
# Register your models here.
admin.site.register(Destination)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)