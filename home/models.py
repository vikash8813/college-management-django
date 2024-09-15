from django.db import models
from django.contrib.auth.models import User
from datetime import timezone

# Create your models here.

class Notifications(models.Model):
    notify_date=models.DateField()
    notify_time=models.TimeField()
    notification=models.CharField(max_length=200)
    notify_by=models.CharField(max_length=70)
    pdfurl=models.URLField(max_length=300,default=None)

class Event(models.Model):
    event_date=models.DateField()
    event_time=models.TimeField(default=None)
    department=models.CharField(max_length=100)
    organiser=models.CharField(max_length=100,default=None)
    location=models.CharField(max_length=70,default=None)
    description=models.TextField()
    email=models.EmailField(default=None)
    phone=models.CharField(max_length=12,default=None)


class Course(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=300)
    description=models.TextField()
    fees=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    subjects=models.CharField(max_length=200)
    department_head=models.CharField(max_length=70)
    semester=models.IntegerField()
    duration=models.CharField(max_length=30)
    eligiblity=models.CharField(max_length=100)
    seats=models.IntegerField(default=100)
    bgein=models.DateField(blank=True,null=True)
    ends=models.DateField(blank=True,null=True)


class Contact(models.Model):
    department=models.CharField(max_length=150)
    phone=models.CharField(max_length=12)
    email=models.EmailField()




class Myusercreate(User):
    checkme=models.BooleanField()

    def __str__(self):
        return (self.username)




class Profile(models.Model):
    user = models.OneToOneField(Myusercreate , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Gallery(models.Model):
    event_image=models.ImageField(upload_to='pics')
    description=models.TextField()


class feedback(models.Model):
    fname=models.CharField(max_length=70)
    umessage=models.TextField()
    feedtime= models.DateTimeField(auto_now_add=True)