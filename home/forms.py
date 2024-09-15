from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Myform(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=Myusercreate
        fields=['username','first_name','last_name','email','password1','password2','checkme']
        labels={'email':'Email','checkme':'Staff','password2':'Re-enter Password'}
        widgets={'username':forms.TextInput({'placeholder':'Enter your username'}),
        'first_name':forms.TextInput({'placeholder':'First name'}),
        'last_name':forms.TextInput({'placeholder':'Last name'}),
        'password1':forms.TextInput({'placeholder':'Enter Password'}),
        'password2':forms.TextInput({'placeholder':'Confirm Password'}),
        'email':forms.TextInput({'placeholder':'Enter your email'}),
        }



        #  widget=forms. TextInput({ "placeholder": "Text!"}))


class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields=['umessage']
        labels={'umessage':'Leave a feedback'} 
        widgets={'umessage':forms.Textarea(attrs={'class':'form-control'})}
        widgets={'umessage':forms.Textarea({'placeholder':'write your comment here'})}


class forogotpasssform(forms.Form):
    username=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter your Username"}))