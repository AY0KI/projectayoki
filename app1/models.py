from django.db import models

# Create your models here.

class item(models.Model):
     name=models.CharField(max_length=100, default='')
     caption=models.CharField(max_length=100, default='')
     image=models.ImageField(upload_to='images/author',default='')
     def __str__(self):
            return f"{self.name}"
     
class contactMsg(models.Model):
    name=models.CharField(max_length=100, default='')
    email=models.TextField(max_length=500, default='')
    def __str__(self):
        return f"{self.name}"
     