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
    if str(response) == "staff mobile":
        res=Student.objects.get(account=request.user)
        res=Staff.objects.get(staffid=res.teacher)
        return HttpResponse(res.phone)
    if str(response) == "mobile":
        res=Student.objects.get(account=request.user)
        if(res):
            return HttpResponse(res.phone)
        s=Staff.objects.get(account=request.user)
        if(s):
            return HttpResponse(s.phone)
    if str(response) == "salary":
        res=Staff.objects.get(account=request.user)
        return HttpResponse(res.salary)
    if str(response) == "staffid":
        res=Staff.objects.get(account=request.user)
        if(res):
            return HttpResponse(res.staffid)
    if str(response) == "rollno":
        res=Student.objects.get(account=request.user)
        return HttpResponse(res.rollno)
    if str(response) == "department":
        res=Student.objects.get(account=request.user)
        if(res):
            res=Staff.objects.get(account=request.user)
        return HttpResponse(res.department)
    if str(response) == "college fee":
        res=CollegeFee.objects.all().values()
        return HttpResponse(res)
    if str(response) == "placements":
        res=Placements.objects.all().values()
        return HttpResponse(res)
    if str(response) == "hostelfee":
        res=HostelFee.objects.all().values()
        return HttpResponse(res)
    if str(response) == "gpa":
        res=Student.objects.get(account=request.user)
        return HttpResponse(res.gpa)
    if str(response) == "attendance":
        res=Student.objects.get(account=request.user)
        return HttpResponse(res.attendance)
    if str(response)!="":
        return HttpResponse(response)       
    return HttpResponse("sorry , i cant unserstand")
           

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
            user.set_password(password)
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