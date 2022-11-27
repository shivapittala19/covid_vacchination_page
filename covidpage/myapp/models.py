from django.db import models
from django.urls import reverse

class MyCovidModel(models.Model):
    city_name= models.CharField(max_length=20, help_text='Enter field documentation')


    def __str__(self):
        return self.city_name

    
    


class MyApplyModel(models.Model):
     
     user_name=models.CharField(max_length=20,help_text='Enter field documentation')
     email=models.EmailField(max_length=40)
     city_name= models.CharField(max_length=20, help_text='Enter field documentation')
     date=models.DateField()

     def __str__(self):
         return self.city_name
