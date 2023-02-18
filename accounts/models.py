from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from datetime import datetime
class Student(models.Model):
    rollno=models.CharField(max_length=20)
    gpa=models.FloatField(null=True)
    department=models.CharField(max_length=20)
    attendance = models.FloatField(null=True)
    account= models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.rollno
    
class Staff(models.Model):
    staffid=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    account= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.staffid
    
class CollegeFee(models.Model):
    department=models.CharField(max_length=20)
    fee= models.FloatField(null=True) 
    def __str__(self):
            return self.department 
    
class Placements(models.Model):
    department=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    package= models.FloatField(null=True) 
    def __str__(self):
            return self.company 
    
class HostelFee(models.Model):
    food=models.CharField(max_length=20)
    ac=models.CharField(max_length=20)
    fee= models.FloatField(null=True) 
    def __str__(self):
            return self.food + self.ac 