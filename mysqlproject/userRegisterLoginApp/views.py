from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Signup


def Home(request):
    return render(request,'Home.html')

def loadSignUp(request):
    return render(request,'SignUp.html')

def loadSignIn(request):
    #get the cookies
    if request.COOKIES.get('usrname'):
        usr=request.COOKIES['usrname']
        psw = request.COOKIES['paswd']
        return render(request,'SignIn.html',{'User':usr,'Pass':psw})
    else:
        return render(request,'SignIn.html')
def loadUserSignIn(request):
    if 'usrdata' in request.session:
        userdata=request.session['usrdata']
        return render(request, 'userprofile.html',{'data':userdata})
    else:
        return render(request,'SignIn.html')
def signup(request):
    if request.method == 'POST':
        vfname=request.POST.get('fname')
        vlname = request.POST.get('lname')
        vuname = request.POST.get('uname')
        vemail = request.POST.get('email')
        vpasswd = request.POST.get('passwd')
        vcpasswd = request.POST.get('cpasswd')
        if(vpasswd==vcpasswd):
            if Signup.objects.filter(username=vuname).exists():
                messages.success(request,"Same Usename....")
                return redirect('/signup')
            elif(Signup.objects.filter(email=vemail).exists()):
                messages.success(request, "Same Email Address....")
                return redirect('/signup')
            else:
                obj=Signup()
                obj.first_name=vfname
                obj.last_name=vlname
                obj.username=vuname
                obj.email=vemail
                obj.password=vpasswd
                obj.save()
                messages.success(request, "Successfully Signed Up....")
                return redirect('/signup')
    else:
        return render(request, 'SignUp.html')
def usersignin(request):
    if request.method=='POST':
        vuname = request.POST.get('uname')
        vpasswd = request.POST.get('passwd')
        newuser= Signup.objects.filter(username=vuname,password=vpasswd).count()
        if (newuser==1):
            request.session['usrdata']=vuname# Session set
            if request.POST.get('chk'):
                #set cookies
                response=redirect('/signin')
                response.set_cookie('usrname',vuname)
                response.set_cookie('paswd', vpasswd)
                return response
            return redirect('/loadigninprofile')
            #return render(request,'userprofile.html',{'data1':newuser})
        else:
            messages.success(request, "Invalid sign in credentials")
            return redirect('/signin')
def userlogout(request):
    request.session.flush()
    return redirect('/signin')