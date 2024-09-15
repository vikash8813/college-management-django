from django.db import models
from home.models import Myusercreate
from django.contrib.auth.models import User

# Create your models here.
class Student_profile(models.Model):
    user=models.OneToOneField(Myusercreate,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=70,null=True,blank=True)
    mother_name=models.CharField(max_length=70,null=True,blank=True)
    phone=models.CharField(max_length=12,null=True,blank=True)
    stu_class=models.CharField(max_length=50,null=True,blank=True)
    semester=models.IntegerField(null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='student_profile')
    DOB=models.DateField(default=None,null=True,blank=True)
    address=models.CharField(max_length=100,default=None,null=True,blank=True)
    stu_age=models.IntegerField(default=None,null=True,blank=True)

class Student_message(models.Model):
    message=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    message_by=models.ForeignKey(User,on_delete=models.CASCADE)
        

class Fine(models.Model):
    reason=models.CharField(max_length=200)
    amount=models.IntegerField()
    status=models.BooleanField()
    last_date=models.DateField(default=None)
    student=models.ForeignKey(User,on_delete=models.CASCADE)

class Pdf(models.Model):
    aboutpdf=models.CharField(max_length=200)
    mainpdf=models.FileField(upload_to='stundent_pdf/',null=True)
    pdf_by=models.CharField(max_length=50,default=None)