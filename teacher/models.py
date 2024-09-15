from django.db import models
from django.contrib.auth.models import User
from home.models import Myusercreate

# Create your models here.
class Teacher_profile(models.Model):
    user=models.OneToOneField(Myusercreate,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=70,null=True,blank=True)
    mother_name=models.CharField(max_length=70,null=True,blank=True)
    phone=models.CharField(max_length=12,null=True,blank=True)
    incharge=models.CharField(max_length=50,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='student_profile')
    DOB=models.DateField(default=None,null=True,blank=True)
    address=models.CharField(max_length=100,default=None,null=True,blank=True)
    teacher_age=models.IntegerField(default=None,null=True,blank=True)
    experience=models.CharField(max_length=20,null=True,blank=True)
    subject_teaches=models.CharField(max_length=50,null=True,blank=True)
    date_join=models.DateField(null=True,blank=True)
