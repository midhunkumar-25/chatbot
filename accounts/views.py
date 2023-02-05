# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
#from .models import Users
# Create your views here.

def index(request):
    return render(request,'index.html')

def studentlogin(request):
    if request.method== 'POST':
        email= request.POST['MailId']
        password = request.POST['password']
        status=request.POST['cap']
        user = User.objects.filter(email=email ,password=password).first()
        if status=="valid" and User.objects.filter(email=email,password=password).exists():
            request.session['profile']={'username':user.username,'MailId':user.email,'Password':user.password}
            userses=request.session['profile']
            request.session.modified=True
            return render(request,'studentchatbot.html',{"userses":userses})
        else:
            messages.info(request,'invalid credentials')
            return render(request,'signinforstudent.html')    

    else:
        return render(request,'signinforstudent.html')   
     
def studentprofile(request):
    user=request.session['profile']
    return render(request,'studentprofile.html',{'user':user}) 

def studentregister(request):
    if request.method == 'POST':
        password=request.POST['createpassword']
        secpassword=request.POST['confirmpassword']
        if password==secpassword:
            for studentitr in User.objects.all():
                if studentitr.username==request.POST['username']:
                    messages.info(request,'username taken')
                    return render(request,'studentregister.html')
                if studentitr.email==request.POST['MailId']:
                    messages.info(request,'email taken')
                    return render(request,'studentregister.html')
            student=User()
            student.username=request.POST['username']
            student.email=request.POST['MailId']
            #student.user.regno=request.POST['regno']
            student.password=password
            student.save()
            return redirect('studentlogin')
        else:
            return render(request,'studentregister.html')
    else:
        return render(request,'studentregister.html')

def logout(request):
    auth.logout(request)
    return redirect('/')  