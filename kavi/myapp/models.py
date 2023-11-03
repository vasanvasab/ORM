from django.db import models
from django.contrib import admin
class Football (models.Model):
    pid=models.CharField(max_length=20,help_text="Employee ID")
    Name=models.CharField(max_length=100)
    Team=models.CharField(max_length=100)
    age=models.IntegerField()
    position=models.CharField(max_length=100)

class FootballAdmin(admin.ModelAdmin):
    list_display=('pid','Name','Team','age','position')
