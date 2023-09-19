from django.contrib import admin
from .models import Chocolate,Category,Cart
# Register your models here.

admin.site.register(Chocolate)
admin.site.register(Category)
admin.site.register(Cart)