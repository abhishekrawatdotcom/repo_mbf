from django.db import models
class EMPMODEL(models.Model):
    name=models.CharField(max_length=50,default=''
                                                )
    password=models.IntegerField(default=0)
    cpassword=models.IntegerField(default=0)
    email=models.EmailField(default='')
    phone=models.IntegerField(default=0)


# Create your models here.
