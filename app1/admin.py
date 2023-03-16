from django.contrib import admin

# Register your models here.
from .models import item,contactMsg
admin.site.register(item)
admin.site.register(contactMsg)