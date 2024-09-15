from django.contrib import admin
# from .models import Notifications,Event,Contact,Course,Myusercreate,Profile
from .models import *

# Register your models here.
@admin.register(Notifications)
class Notificationadmin(admin.ModelAdmin):
    list_display=['id','notify_date','notify_time','notification','notify_by']


@admin.register(Event)
class Eventadmin(admin.ModelAdmin):
    list_display=['id','department','description','organiser','event_date','event_time','location']



@admin.register(Contact)
class Eventadmin(admin.ModelAdmin):
    list_display=['id','department','phone','email']



@admin.register(Course)
class Eventadmin(admin.ModelAdmin):
    list_display=['id','name','title','description','fees','email','phone','subjects','department_head','semester','duration','eligiblity']



# Register your models here.


admin.site.register(Profile)
# admin.site.register(Myusercreate)
@admin.register(Myusercreate)
class Myuseradmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','email','checkme']


@admin.register(Gallery)
class Galleryadmin(admin.ModelAdmin):
    list_display=['id','event_image','description']


@admin.register(feedback)
class feedbackadmin(admin.ModelAdmin):
    list_display = ['id','umessage','fname','feedtime']