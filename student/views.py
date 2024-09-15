from django.shortcuts import render
from . models import *
from home.models import Myusercreate
from . forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from home.models import Notifications
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash,logout

# Create your views here.



@login_required(login_url='/login/')
def profile_edit(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        studentmoredtails=Myusercreate.objects.get(username=request.user.username)    
        student=Student_profile.objects.get(user__username=request.user.username)
        
        initials={'username':studentmoredtails.username,'first_name':studentmoredtails.first_name,'last_name':studentmoredtails.last_name,'age':student.stu_age,'email':studentmoredtails.email,'father_name':student.father_name,'mother_name':student.mother_name,'student_class':student.stu_class,'semester':student.semester,'DOB':student.DOB,'address':student.address,'phone':student.phone}
        if request.method=='POST':
            fm=Studentprofileform(request.POST,request.FILES,initial=initials)
            # uname=request.POST['username']
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
                return HttpResponseRedirect('/student/profile/')
        else:
            fm=Studentprofileform(initial=initials)
        context={'profile':'present','profilea':'present-color','form':fm,'student':student,'studentmore':studentmoredtails}
        return render(request,'student/profileedit.html',context)




@login_required(login_url='/login/')
def student_profile(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        studentmoredtails=Myusercreate.objects.get(username=request.user.username)    
        student=Student_profile.objects.get(user__username=request.user.username)
        context={'student':student,'studentmore':studentmoredtails,'profile':'present','profilea':'present-color'}
        return render(request,'student/profile.html',context)


@login_required(login_url='/login/')
def icard(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        studentmoredtails=Myusercreate.objects.get(username=request.user.username)    
        student=Student_profile.objects.get(user__username=request.user.username)
        context={'icard':'present','icarda':'present-color','student':student,'studentmore':studentmoredtails}
        return render(request,'student/icard.html',context)

@login_required(login_url='/login/')
def student_passchange(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        studentmoredtails=Myusercreate.objects.get(username=request.user.username)    
        student=Student_profile.objects.get(user__username=request.user.username)
        if request.method=='POST':
            fm=Mypasschangeform(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully')
                return HttpResponseRedirect('/student/profile/')
        else:
            fm=Mypasschangeform(user=request.user)
        context={'student':student,'studentmore':studentmoredtails,'passchange':'present','passchangea':'present-color','form':fm}
        return render(request,'student/passchange.html',context)

@login_required(login_url='/login/')
def student_notifications(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        studentmoredtails=Myusercreate.objects.get(username=request.user.username)    
        student=Student_profile.objects.get(user__username=request.user.username)
        allnotifications=Notifications.objects.order_by('-id')
        allmessages=Student_message.objects.order_by('-id')
        context={'student':student,'studentmore':studentmoredtails,'notify':'present','notifya':'present-color','allnotifications':allnotifications,'allmessages':allmessages}
        return render(request,'student/notifications.html',context)

@login_required(login_url='/login/')
def student_pdf(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        studentmoredtails=Myusercreate.objects.get(username=request.user.username)
        student=Student_profile.objects.get(user__username=request.user.username)
        pdfs=Pdf.objects.order_by('-id')
        context={'pdf':'present','pdfa':'present-color','studentmore':studentmoredtails,'student':student,'pdfs':pdfs}
        return render(request,'student/pdf.html',context)

@login_required(login_url='/login/')
def student_fine(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        studentmoredtails=Myusercreate.objects.get(username=request.user.username)    
        student=Student_profile.objects.get(user__username=request.user.username)
        fines=Fine.objects.filter(student__username=request.user.username)
        unpaidfine=fines.filter(status=False)
        totalfine=0
        for i in unpaidfine:
            totalfine=totalfine+i.amount
        context={'student':student,'studentmore':studentmoredtails,'fine':'present','finea':'present-color','fines':fines,'total':totalfine}
        return render(request,'student/fine.html',context)

@login_required(login_url='/login/')
def student_logout(request):
    if request.user.is_staff:
        messages.warning(request,'You are not a student')    
        return HttpResponseRedirect('/')
    else:
        logout(request)
        return HttpResponseRedirect('/')

