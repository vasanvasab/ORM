# Ex02 Django ORM Web Application
## Date: 02.11.2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
Admin.py

from django.contrib import admin
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)

Models.py

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

```

## OUTPUT
![Screenshot 2023-11-03 214358](https://github.com/vasanvasab/ORM/assets/143481226/041409be-3a68-4848-bc68-3c96fd21be0c)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
