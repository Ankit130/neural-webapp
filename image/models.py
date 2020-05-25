from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_image = models.ImageField(upload_to='upload/')
    emp_image2=models.ImageField(upload_to='style/')