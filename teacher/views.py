from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import Myusercreate
from .models import *
from . forms import *
from student.forms import Studentprofileform
from django.contrib.auth import update_session_auth_hash,logout
from student.models import Pdf,Student_message,Student_profile,Fine
from home.models import Notifications,Course
import datetime

# Create your views here.

@login_required(login_url='/login/')
def teacher_profile(request):
    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)    
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        context={'student':teacher,'studentmore':teachermoredetails,'profile':'present','profilea':'present-color','profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/profile.html',context)

    else:
        messages.warning(request,'You are not a Staff')    
        return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def teacher_logout(request):
    if request.user.is_staff:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        messages.warning(request,'You are not Staff')
        return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def profile_edit(request):

    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)    
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        
        initials={'username':teachermoredetails.username,'first_name':teachermoredetails.first_name,'last_name':teachermoredetails.last_name,'age':teacher.teacher_age,'email':teachermoredetails.email,'father_name':teacher.father_name,'mother_name':teacher.mother_name,'experienc':teacher.experience,'date_join':teacher.date_join,'DOB':teacher.DOB,'address':teacher.address,'phone':teacher.phone,
        'subject_teaches':teacher.subject_teaches,'incharge':teacher.incharge}
        if request.method=='POST':
            fm=Teacherprofileform(request.POST,request.FILES,initial=initials)
            # uname=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            father_name=request.POST['father_name']
            mother_name=request.POST['mother_name']
            age=request.POST['age']
            experience=request.POST['experience']
            address=request.POST['address']
            DOB=request.POST['DOB']
            date_join=request.POST['date_join']
            incharge=request.POST['incharge']
            subject_teaches=request.POST['subject_teaches']
            profile_pic=request.FILES.get('profile_pic')
            phone=request.POST['phone']
            if fm.is_valid():
                teachermoredetails.first_name=first_name
                teachermoredetails.last_name=last_name
                teachermoredetails.save()
                teacher.father_name=father_name
                teacher.mother_name=mother_name
                teacher.teacher_age=age
                teacher.experience=experience
                teacher.date_join=date_join
                teacher.subject_teaches=subject_teaches
                teacher.incharge=incharge
                teacher.address=address
                if profile_pic:
                    teacher.profile_pic=profile_pic
                teacher.DOB=DOB
                teacher.phone=phone
                teacher.save()
                messages.success(request,'Profile Updated Successfully!!!')
                return HttpResponseRedirect('/teacher/profile/')
        else:
            fm=Teacherprofileform(initial=initials)
        context={'profile':'present','profilea':'present-color','form':fm,'student':teacher,'studentmore':Teacherprofileform,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/profileedit.html',context)
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def icard(request):
    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)    
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        context={'icard':'present','icarda':'present-color','student':teacher,'studentmore':teachermoredetails,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/icard.html',context)
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def teacher_passchange(request):

    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)    
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        if request.method=='POST':
            fm=Mypasschangeform(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully')
                return HttpResponseRedirect('/teacher/profile/')
        else:
            fm=Mypasschangeform(user=request.user)
        context={'student':teacher,'studentmore':teachermoredetails,'passchange':'present','passchangea':'present-color','form':fm,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/passchange.html',context)
    
    else: 
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def teacher_pdf(request):

    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        pdfs=Pdf.objects.order_by('-id')
        context={'pdf':'present','pdfa':'present-color','studentmore':teachermoredetails,'student':teacher,'pdfs':pdfs,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/pdf.html',context)


    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def notifications(request):
    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        if request.method == 'POST':
            fm=Notificationform(request.POST,request.FILES)
            if fm.is_valid():
                notify_date=fm.cleaned_data['notify_date']
                notification=fm.cleaned_data['notification']
                pdfurl=fm.cleaned_data['pdfurl']
                notifydata=Notifications(notify_date=notify_date,notification=notification,pdfurl=pdfurl,notify_by=request.user.username,notify_time=datetime.datetime.now())
                notifydata.save()
                messages.success(request,'Notification added Successfully')
                return HttpResponseRedirect('/teacher/notifications/')
        else:
            fm=Notificationform()
        allnotifications=Notifications.objects.order_by('-id')
        context={'notifyb':'present','notifyba':'present-color','studentmore':teachermoredetails,'student':teacher,'allnotifications':allnotifications,'form':fm,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/notification.html',context)

    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')



@login_required(login_url='/login/')
def message(request):
    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        if request.method == 'POST':
            fm=Messageform(request.POST)
            print("Inside post")
            if fm.is_valid():
                message=fm.cleaned_data['message']
                notifydata=Student_message.objects.create(message=message,message_by=request.user)
                notifydata.save()
                messages.success(request,'Message added Successfully')
                return redirect('/teacher/addmessages/')
        else:
            fm=Messageform()
        allmessages=Student_message.objects.order_by('-id')
        context={'addmsg':'present','addmsga':'present-color','studentmore':teachermoredetails,'student':teacher,'allmessages':allmessages,'form':fm,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/addmessage.html',context)

    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def teacher_addpdf(request):

    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        if request.method=="POST":
            fm=Pdfform(request.POST,request.FILES)
            if fm.is_valid():
                aboutpdf=fm.cleaned_data['aboutpdf']
                mainpdf=fm.cleaned_data['mainpdf']
                pdfdata=Pdf(aboutpdf=aboutpdf,mainpdf=mainpdf,pdf_by=request.user.username)
                pdfdata.save()
                messages.success(request,'Pdf added Successfully')
                return HttpResponseRedirect('/teacher/pdfs/')
        else:
            fm=Pdfform()
        context={'pdf':'present','pdfa':'present-color','studentmore':teachermoredetails,'student':teacher,'form':fm,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/addpdf.html',context)
    
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def pdf_delete(request,id):
    if request.user.is_staff:
        user_id=Pdf.objects.get(pk=id)
        user_id.delete()
        messages.warning(request,'Pdf deleted')
        return HttpResponseRedirect('/teacher/pdfs/')
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def notify_delete(request,id):
    if request.user.is_staff:
        user_id=Notifications.objects.get(pk=id)
        user_id.delete()
        messages.warning(request,'Notification deleted')
        return HttpResponseRedirect('/teacher/notifications/')
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')




@login_required(login_url='/login/')
def message_delete(request,id):
    if request.user.is_staff:
        user_id=Student_message.objects.get(pk=id)
        user_id.delete()
        messages.warning(request,'Message deleted')
        return HttpResponseRedirect('/teacher/addmessages/')
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')



@login_required(login_url='/login/')
def studentsedit(request):
    if request.user.is_staff:
        teachermoredetails=Myusercreate.objects.get(username=request.user.username)
        teacher=Teacher_profile.objects.get(user__username=request.user.username)
        profile_pic=teacher.profile_pic
        user_name=teachermoredetails.get_full_name
        allstudents=Myusercreate.objects.filter(is_staff=False)
        print(allstudents)
        context={'stu':'present','stua':'present-color','studentmore':teachermoredetails,'student':teacher,'allstudents':allstudents,'profile_pic':profile_pic,'user_name':user_name}

        return render(request,'teacher/students.html',context)
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/') 



@login_required(login_url='/login/')
def student_profile_edit(request,username):
    if request.user.is_staff:
        studentmoredtails=Myusercreate.objects.get(username=username)    
        student=Student_profile.objects.get(user__username=username)
        profile_pic=Teacher_profile.objects.get(user__username=request.user.username).profile_pic
        user_name=Myusercreate.objects.get(username=request.user.username).get_full_name
        
        initials={'username':studentmoredtails.username,'first_name':studentmoredtails.first_name,'last_name':studentmoredtails.last_name,'age':student.stu_age,'email':studentmoredtails.email,'father_name':student.father_name,'mother_name':student.mother_name,'student_class':student.stu_class,'semester':student.semester,'DOB':student.DOB,'address':student.address,'phone':student.phone}
        if request.method=='POST':
            fm=Studentprofileform(request.POST,request.FILES,initial=initials)
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            father_name=request.POST['father_name']
            mother_name=request.POST['mother_name']
            age=request.POST['age']
            student_class=request.POST['student_class']
            address=request.POST['address']
            DOB=request.POST['DOB']
            profile_pic=request.FILES.get('profile_pic')
            phone=request.POST['phone']
            if fm.is_valid():
                studentmoredtails.first_name=first_name
                studentmoredtails.last_name=last_name
                studentmoredtails.save()
                student.father_name=father_name
                student.mother_name=mother_name
                student.stu_age=age
                student.stu_class=student_class
                student.address=address
                if profile_pic:
                    student.profile_pic=profile_pic
                student.DOB=DOB
                student.phone=phone
                student.save()
                messages.success(request,'Profile Updated Successfully!!!')
                return HttpResponseRedirect('/teacher/studentinfo/')
        else:
            fm=Studentprofileform(initial=initials)
        context={'stu':'present','stua':'present-color','form':fm,'student':student,'studentmore':studentmoredtails,'profile_pic':profile_pic,'user_name':user_name}
        return render(request,'teacher/studentedit.html',context)

    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/') 

@login_required(login_url='/login/')
def student_fine(request,username):
    if request.user.is_staff:
        studentmoredtails=Myusercreate.objects.get(username=username)    
        student=Student_profile.objects.get(user__username=username)
        profile_pic=Teacher_profile.objects.get(user__username=request.user.username).profile_pic
        user_name=Myusercreate.objects.get(username=request.user.username).get_full_name
        fines=Fine.objects.filter(student__username=username).reverse()
        fineid=Myusercreate.objects.get(username=username)
        print(fineid.id)
        unpaidfine=fines.filter(status=False)
        totalfine=0
        for i in unpaidfine:
            totalfine=totalfine+i.amount
        if request.method=="POST":
            fm=Fineform(request.POST)
            if fm.is_valid():
                reason=fm.cleaned_data['reason']
                amount=fm.cleaned_data['amount']
                last_date=fm.cleaned_data['last_date']
                Fine(reason=reason,amount=amount,status=False,last_date=last_date,student=fineid).save()
                fm=Fineform()
                return redirect(f'/teacher/addfine/{username}')
        else:
            fm=Fineform()
        context={'student':student,'studentmore':studentmoredtails,'fine':'present','finea':'present-color','fines':fines,'total':totalfine,'profile_pic':profile_pic,'user_name':user_name,'form':fm}
        return render(request,'teacher/fine.html',context)

    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/') 


@login_required(login_url='/login/')
def events(request):
    if request.user.is_staff:
        profile_pic=Teacher_profile.objects.get(user__username=request.user.username).profile_pic
        user_name=Myusercreate.objects.get(username=request.user.username).get_full_name
        allevents=Event.objects.order_by('-id')
        if request.method=='POST':
            fm=Eventform(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm=Eventform()
        context={'addevent':'present','addeventa':'present-color','profile_pic':profile_pic,'user_name':user_name,'form':fm,'allevents':allevents}
        return render(request,'teacher/events.html',context)

@login_required(login_url='/login/')
def event_delete(request,id):
    if request.user.is_staff:
        user_id=Event.objects.get(pk=id)
        user_id.delete()
        messages.warning(request,'Event deleted')
        return HttpResponseRedirect('/teacher/addevents/')
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')



@login_required(login_url='/login/')
def addcourse(request):
    if request.user.is_staff:
        profile_pic=Teacher_profile.objects.get(user__username=request.user.username).profile_pic
        user_name=Myusercreate.objects.get(username=request.user.username).get_full_name
        allcourses=Course.objects.order_by('-id')
        if request.method=='POST':
            fm=Courseform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'New course added successfully')
                return HttpResponseRedirect('/teacher/addcourse/')
        else:
            fm=Courseform()
        context={'addcourse':'present','addcoursea':'present-color','profile_pic':profile_pic,'user_name':user_name,'form':fm,'allcourses':allcourses}
        return render(request,'teacher/addcourse.html',context)


@login_required(login_url='/login/')
def course_delete(request,id):
    if request.user.is_staff:
        user_id=Course.objects.get(pk=id)
        user_id.delete()
        messages.warning(request,'Course deleted')
        return HttpResponseRedirect('/teacher/addcourse/')
    else:
        messages.warning(request,'You are not a staff')    
        return HttpResponseRedirect('/')