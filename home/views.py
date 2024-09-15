from django.shortcuts import render
from . models import Notifications,Event,Contact,Course
from .models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseRedirect
from student.models import Student_profile
from teacher.models import Teacher_profile
from django.contrib.auth.forms import SetPasswordForm
# Create your views here.

forgot_user_list=['user']

def home(request):
    allnotifications=Notifications.objects.order_by('-id')
    events=Event.objects.order_by('-id')
    courses=Course.objects.order_by('-id')
    return render(request,'home/home.html',{'allnotifications':allnotifications,'events':events,'courses':courses})

def events(request,id):
    event_id=Event.objects.get(pk=id)
    return render(request,'home/events.html',{'event':event_id}) 


def admission(request):
    # course_id=Course.objects.get(pk=id)
    return render(request,'home/admission.html')

def course(request,id):
    course_id=Course.objects.get(pk=id)
    return render(request,'home/course.html',{'course':course_id}) 
# @login_required
# def home(request):
#     return render(request , 'home.html')







def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.warning(request, 'User not found.')
            return redirect('/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.warning(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.warning(request, 'Wrong password.')
            return redirect('/login')
        usercheckme=Myusercreate.objects.get(username=username).checkme
        print(usercheckme)
        if usercheckme and not user_obj.is_staff:
            messages.warning(request,'your Staff request is not verified yet')
            return redirect('/')
        if usercheckme and user_obj.is_staff:
            login(request,user)
            email=request.user.email
            send_mail_after_login(email,username)
            return redirect('/teacher/profile/')
        if usercheckme==False:
            login(request , user)
            email=request.user.email
            send_mail_after_login(email,username)
            return redirect('/student/profile/')
    return render(request , 'home/login.html')

def register_attempt(request):

    if request.method == 'POST':
        fm=Myform(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')        
        fname = request.POST.get('first_name')        
        lname = request.POST.get('last_name')        
        password = request.POST.get('password2')        
        checkbox1=request.POST.get('checkme')
        if checkbox1=='on':
            mycheck=True
        else:
            mycheck=False

        try:
            if User.objects.filter(username = username).first():
                messages.warning(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.warning(request, 'Email is taken.')
                return redirect('/register')
            print(fm.is_valid())
            if fm.is_valid():
                # fm.save()
            
                # user_obj = User(username = username , email = email)
                user_obj=Myusercreate(username=username,email=email,first_name=fname,last_name=lname,checkme=mycheck)
                user_obj.set_password(password)
                print(user_obj)
                user_obj.save()
                if checkbox1!='on':
                    student_profile_obj=Student_profile.objects.create(user=user_obj)
                    student_profile_obj.save()
                else:
                    teacher_profile_obj=Teacher_profile.objects.create(user=user_obj)
                    teacher_profile_obj.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
                profile_obj.save()
                send_mail_after_registration(email , auth_token)
                messages.success(request,'A mail has been sent to your email. please check your email.')
                return redirect('/register')

        except Exception as e:
            print(e)
    
    else:
        fm=Myform()


    return render(request , 'home/register.html',{'form':fm})





def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            messages.warning(request,'your mail is not verified')
            return redirect('/login')
    except Exception as e:
        print(e)
        return redirect('/')

# def error_page(request):
#     return  render(request , 'error.html')


def forgot_password(request):
    if request.method=="POST":
        fm=forogotpasssform(request.POST)
        if fm.is_valid():
            forgot_user=fm.cleaned_data['username']
            # print(forgot_user)
            profile_obj=Myusercreate.objects.filter(username=forgot_user)
            if profile_obj:
                print('mail send hui')
                # print(forgot_username)
                forgot_user_list[0]=forgot_user
                print(forgot_user_list)

                # global forgot_username
                # forgot_username=10
                # print(usernmae_forgot)
                return HttpResponseRedirect('/changeforgot/')
            else:
                messages.warning(request,"Username does'nt exists")
                return HttpResponseRedirect('/forgotpass/')
    else:
        fm=forogotpasssform()
    return render(request,"home/forgotpass.html",{'form':fm})

def changeforgot(request):
    if request.method=="POST":
        fm=SetPasswordForm(request.user.forgot_user_list[0])
    else:
        print(forgot_user_list[0])
        fm=SetPasswordForm(request.user.forgot_user_list[0])
    
    return render(request,'home/changeforgot.html',{'form':fm})








def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi click the link to verify your account http://127.0.0.1:8000/login/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


def send_mail_after_login(email,username):
    subject = 'account log in'
    message = f'You have successfully login in Cranfield University with  {username}'
    email_from = settings.EMAIL_HOST_USER
    # print('user log in ho gya')
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def send_mail_for_forgot_password(email,token):
    subject='Forgot Password'
    message=f"plesae click the link to reset your password http://127.0.0.1:8000/login/{token}"
    email_from= settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)

def gallery(request):
    firstdata=Gallery.objects.order_by('-id')[0]
    seconddata=Gallery.objects.order_by('-id')[1]
    thirddata=Gallery.objects.order_by('-id')[2]
    # print(firstdata)
    return render(request,'home/gallery.html',{'event1':firstdata,'event2':seconddata,'event3':thirddata})



def feedbackdata(request):
    if request.method == 'POST':
        fm = feedbackform(request.POST)
        if fm.is_valid():
            feed=fm.cleaned_data['umessage']
            # ip=request.META.get('REMOTE_ADDR')
            # req=feedback(fname=request.user,umessage=feed)
            req=feedback(umessage=feed)
            req.save()
            messages.success(
                request, 'Feedback has been submited successfully!!!')
            return HttpResponseRedirect('/feedback/')

    else:
        fm = feedbackform()
    stud=feedback.objects.order_by('-id')

    return render(request, 'home/feedback.html', {'stud':stud,'form': fm})


def staffs(request):
    return render(request,'home/staffs.html')