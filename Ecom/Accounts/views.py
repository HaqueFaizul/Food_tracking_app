from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def loadRegister(request):
    return render(request,'register.html')
def loadLogin(request):
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        vfname = request.POST.get('fname')
        vlname = request.POST.get('lname')
        vuname = request.POST.get('uname')
        vemail = request.POST.get('email')
        vpasswd = request.POST.get('passwd')
        vcpasswd = request.POST.get('cpasswd')
        if vpasswd == vcpasswd:
            if User.objects.filter(username=vuname).exists():
                messages.success(request, 'Username already exist')
                return redirect('/')
            elif User.objects.filter(email=vemail).exists():
                messages.success(request, 'Email address is already registered..')
                return redirect('/')
            else:
                newuser = User.objects.create_user(first_name=vfname, last_name=vlname, username=vuname, email=vemail,
                                   password=vpasswd)
                newuser.save()
                messages.success(request, 'You have successfully registered')
                return render(request,'login.html')
                #return redirect('/userlogin')
        else:
            messages.success(request, 'Password is not matching....')
            return redirect('/')
    else:
        return render(request, 'Registration.html')
def userlogin(request):
    if request.method == 'POST':
        vuname = request.POST.get('uname')
        vpasswd = request.POST.get('passwd')
        #print(vuname,vpasswd)
        #exit()
        newuser=auth.authenticate(username=vuname,password=vpasswd)
        if newuser is not None:
            auth.login(request,newuser)
            return redirect('/home')
            #return render(request,'HomePage.html')
        else:
            return render(request,'register.html')
@login_required(login_url='userlogin')
def logout(request):
    auth.logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('/account/loadlogin')



