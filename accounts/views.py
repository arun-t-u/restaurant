from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print('login')
            return redirect('/')
        else:
            return redirect('register')    
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # Password Verification
        if password == confirm_password:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request,"Username or Email already taken")
                return redirect('register')
            else:
            # Add to database
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matched")
            return redirect('register')
    else:
        return render(request,'registration.html')

