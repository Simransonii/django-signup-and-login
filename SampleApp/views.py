from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages 
# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    
    if request.method=="POST":
        
        # username=request.POST.get("username")
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        
        myuser.save()
        
        messages.success(request,"You account is created Successfully lo")
        
        return redirect('signin')
    
    
    
    return render(request,'signup.html')

def signin(request):
    
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        
        user=authenticate(username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'home.html',{'fname':fname})
        else:
            messages.error(request,"Bad crediantials 00")
            return redirect('index')
        
    return render(request,'signin.html')

def home(request):
    return render (request,'home.html')

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('index')