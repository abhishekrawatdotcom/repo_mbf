from django.contrib import admin
from webapp.models import EMPMODEL

class ADMINMODEL(admin.ModelAdmin):
    list_display = ['name','password','cpassword','email','phone']
admin.site.register(EMPMODEL,ADMINMODEL)

# Register your models here.
