from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def HomePage(request):
    return render(request,'HomePage.html')

def LoadRegister(request):
    return render(request,'Registration.html')

def Loadlogin(request):
    return render(request,'login.html')
def Loaduserprofile(request):
    if request.user.is_authenticated:
        return render(request, 'userprofile.html')
    else:
        return redirect('/loadlogin')
def register(request):
    if request.method=='POST':
        vfname=request.POST.get('fname')
        vlname = request.POST.get('lname')
        vuname = request.POST.get('uname')
        vemail = request.POST.get('email')
        vpasswd = request.POST.get('passwd')
        vcpasswd = request.POST.get('cpasswd')
        if vpasswd == vcpasswd:
            if User.objects.filter(username=vuname).exists():
                messages.success(request, 'Username already exist')
                return redirect('/registration')
            elif User.objects.filter(email=vemail).exists():
                messages.success(request, 'Email address is already registered..')
                return redirect('/registration')
            else:
                newuser=User.objects.create_user(first_name=vfname,last_name=vlname,username=vuname,email=vemail,password=vpasswd)
                newuser.save()
                messages.success(request,'You have successfully registered')
                return redirect('/registration')
        else:
            messages.success(request, 'Password is not matching....')
            return redirect('/registration')
    else:
        return render(request,'Registration.html')
def userlogin(request):
    if request.method == 'POST':
        vuname = request.POST.get('uname')
        vpasswd = request.POST.get('passwd')
        newuser=auth.authenticate(username=vuname,password=vpasswd)
        if newuser is not None:
            auth.login(request,newuser)
            return redirect('/userprofile')
            #messages.success(request, 'Logged in successfully')
            #return render(request,'userprofile.html',{'user':newuser})
        else:
            return render(request,'Registration.html')
def userlogout(request):
    auth.logout(request)
    return redirect('/loadlogin')

