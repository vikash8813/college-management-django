from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Teacher_profile)
class Teacheradmin(admin.ModelAdmin):
    list_display=['id','father_name','mother_name','phone','experience','date_join','DOB','address','subject_teaches','incharge','user']
