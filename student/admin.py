from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Student_profile)
class Studentadmin(admin.ModelAdmin):
    list_display=['id','father_name','mother_name','phone','stu_class','semester','DOB','address','user']

@admin.register(Student_message)
class Studentmessageadmin(admin.ModelAdmin):
    list_display=['id','message','date','message_by']


@admin.register(Fine)
class Fineadmin(admin.ModelAdmin):
    list_display=['id','reason','amount','status','student']


@admin.register(Pdf)
class Pdfadmin(admin.ModelAdmin):
    list_display=['id','aboutpdf','mainpdf','pdf_by']





