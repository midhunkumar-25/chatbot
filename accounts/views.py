# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Student,Staff,CollegeFee,Placements,HostelFee
from .bot import classify_intent
#from .models import Users
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginMethod(request):
    if request.method== 'POST':
        print("login consol")
        print(request.user)
        email= request.POST['MailId']
        password = request.POST['password']
        userobj = User.objects.filter(email=email).first()   
        user = authenticate(username=userobj.username,password=password)
        if user is not None:
            login(request, user)
            return redirect('../chat')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'signinforstudent.html')    

    else:
        return render(request,'signinforstudent.html')   

def chatbotPage(request):
     if request.user.is_authenticated:
        return render(request,'studentchatbot.html',{'user':request.user})  
     else:
        return redirect('login')
     
def chatbotquery(request):
    response =classify_intent(request.body.decode('ASCII'))
    print(str(response))
    if str(response) == "college fee":
        res=CollegeFee.objects.all().values()
        return HttpResponse(res)
    if str(response) == "placements":
        res=Placements.objects.all().values()
        return HttpResponse(res)
    if str(response) == "hostelfee":
        res=HostelFee.objects.all().values()
        return HttpResponse(res)
    
        
    return HttpResponse(response)
           

def studentprofile(request):
    user=request.session['profile']
    return render(request,'studentprofile.html',{'user':user}) 

def registerMethod(request):
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
            user=User()
            user.username=request.POST['username']
            user.email=request.POST['MailId']
            #student.user.regno=request.POST['regno']
            user.password=password
            user.save()
            if request.POST['type'] == "Student":
                student=Student()
                student.rollno=request.POST['id'] 
                student.department=request.POST['department'] 
                student.account=user
                student.save()
            if request.POST['type'] == "Staff":
                staff=Staff()
                staff.staffid=request.POST['id'] 
                staff.department=request.POST['department'] 
                staff.account=user
                staff.save()
            return redirect('login')
        else:
            return render(request,'studentregister.html')
    else:
        return render(request,'studentregister.html')

def logoutMethod(request):
    logout(request)
    return redirect('login')  