from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class Studentprofileform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    father_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Father's Name")
    mother_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Mother's Name",required=False)
    age=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    student_class=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),)
    semester=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    DOB=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
    profile_pic=forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'myimg'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)

    field_order=['username','email']


class Mypasschangeform(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='New Password')
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')



