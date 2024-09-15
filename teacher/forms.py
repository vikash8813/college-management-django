from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from  student.models import Pdf
from home.models import Notifications,Event,Course
from student.models import Student_message,Fine

class Teacherprofileform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    father_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Father's Name")
    mother_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Mother's Name",required=False)
    age=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    incharge=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    experience=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    DOB=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}))
    profile_pic=forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'myimg'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    subject_teaches=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    date_join=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}))


    field_order=['username','email']


class Mypasschangeform(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='New Password')
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')

class Pdfform(forms.ModelForm):
    class Meta:
        model=Pdf
        fields=['aboutpdf','mainpdf']
        widgets={'aboutpdf':forms.TextInput(attrs={'class':'form-control'})}
        labels={'aboutpdf':'About Pdf','mainpdf':'Add File'}




class Notificationform(forms.ModelForm):
    class Meta:
        model=Notifications
        fields=['notify_date','notification','pdfurl']
        widgets={'notification':forms.TextInput(attrs={'class':'form-control'}),'pdfurl':forms.TextInput(attrs={'class':'form-control'}),'notify_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Y-M-D'})}
        labels={'notify_date':'Notification Date','notification':'Notification','pdfurl':'Pdf url'}



class Messageform(forms.ModelForm):
    class Meta:
        model=Student_message
        fields=['message']
        widgets={'message':forms.TextInput(attrs={'class':'form-control'})}
        labels={'message':'Student Message'}



class Fineform(forms.ModelForm):
    class Meta:
        model=Fine
        fields=['reason','amount','last_date']
        widgets={'reason':forms.TextInput(attrs={'class':'form-control'}),'last_date':forms.TextInput(attrs={'class':'form-control'})}



class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'
        widgets={'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),'event_time':forms.TextInput(attrs={'class':'form-control'}),'department':forms.TextInput(attrs={'class':'form-control'}),'organiser':forms.TextInput(attrs={'class':'form-control'}),'location':forms.TextInput(attrs={'class':'form-control'}),'description':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'}),'phone':forms.TextInput(attrs={'class':'form-control'})}





class Courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'title':forms.TextInput(attrs={'class':'form-control'}),'fees':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'}),'phone':forms.TextInput(attrs={'class':'form-control'}),'subjects':forms.TextInput(attrs={'class':'form-control'}),'department_head':forms.TextInput(attrs={'class':'form-control'}),'semester':forms.TextInput(attrs={'class':'form-control'}),'duration':forms.TextInput(attrs={'class':'form-control'}),'eligiblity':forms.TextInput(attrs={'class':'form-control'}),'seats':forms.TextInput(attrs={'class':'form-control'}),'bgein':forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),'ends':forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),'description':forms.Textarea(attrs={'class':'form-control'})}





