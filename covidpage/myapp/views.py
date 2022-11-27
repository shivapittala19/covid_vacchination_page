from django.shortcuts import render,redirect
from django.db.models import Count
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import MyCovidModel,MyApplyModel
from datetime import date
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        FirstName=request.POST['FirstName']
        LastName=request.POST['LastName']
        EmailId=request.POST['EmailID']
        UserName=request.POST['UserName']
        Password=request.POST['Password']
        ConfirmPassword=request.POST['ConfirmPassword']
        if Password==ConfirmPassword:
            if User.objects.filter(username=UserName).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=EmailId).exists():
                messages.info(request,'emailid already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=UserName,email=EmailId,password=Password,first_name=FirstName,last_name=LastName)
                user.save()
                print('user created sucesfully')
        else:
            print('passwor is not matching')
            return redirect('register')
        return redirect('login_user') 
    else:
        return render(request,'register.html')
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)  
        if user is not None:
            login(request,user)
            return render(request,'search.html')
        else:
            messages.info(request,"Invalid credentials")
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def search(request):
    if request.method=='POST':
        city=request.POST['Search']
        if city is not None:
            res=MyCovidModel.objects.filter(city_name__icontains=city).distinct()
            city_Found=False
            for query in res:
                if query.city_name.lower()==city.lower():
                    city_Found=True   
            if city_Found:
                return redirect('apply')     
            else:
                messages.info(request,'City not available ! search for another city')
                return render(request,'search.html')
        else:  
            return render(request,'search.html')
    results=MyCovidModel.objects.all()
    return render(request,'search.html',{"city":results})
    
def apply(request):
    if request.method=='POST':
        data=MyApplyModel()
        Date=request.POST['Date']
        city=request.POST['City']
        user_name=request.POST['user_name']
        email=request.POST['email']
        fieldname ='date'
        x=MyApplyModel.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))
        res=0
        for  query in x:
            if query['date'].strftime("%Y-%m-%d")==Date:
                res=query['the_count']
                print(res)
                break
        if Date < date.today().strftime("%Y-%m-%d"):
            messages.info(request,"Choose Date from today onwards")
            return render(request,'apply.html')
        elif res>10:
            messages.info(request,"Current date Vacchination limit exceeded!.Choose another Date")
            return render(request,'apply.html')
        elif MyApplyModel.objects.filter(email=email).exists():
            messages.info(request,"Email alredy registered")
            return render(request,'apply.html')
        else:
            data.user_name=user_name
            data.email=email
            data.city_name=city
            data.date=Date
            data.save()
            messages.info(request,'sucessfully applied for vacchination')
            return render(request,'apply.html')
    results=MyCovidModel.objects.all()
    return render(request,'apply.html',{"city":results})
def logout_user(request):
    logout(request)
    return redirect('/')



