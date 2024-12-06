from django.db import models

# Create your models here.

class Users(models.Model):
    title = models.CharField(max_length = 70,blank = False,default = '')
    description = models.CharField(max_length = 70,blank = False,default = '')
    created_at=models.DateTimeField()
    completed=models.BooleanField()

