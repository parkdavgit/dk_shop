from django.contrib import admin
from .models import Destination, Cart, Allorder, Checkorder
# Register your models here.
admin.site.register(Destination)
admin.site.register(Cart)
admin.site.register(Allorder)
admin.site.register(Checkorder)