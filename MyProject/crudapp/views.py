from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student


def loadStudent(request):
    std=StudentForm()
    return render(request,'StudentForm.html',{'data':std})
def insertStudent(request):
    if request.method=='POST':
        std = StudentForm(request.POST)
        if (std.is_valid()):
            std.save()
            return redirect('/display')#redirecting to the root path
    else:
        return render(request,'StudentForm.html')
def displayStudent(request):
    stddata=Student.objects.all()
    return render(request,"DisplayStudent.html",{'data':stddata})

def destroyStudent(request,sid):
    stddata=Student.objects.get(id=sid)
    stddata.delete()
    return redirect('/')

def EditStudent(request,sid):
    if request.method=='POST':
        stddata = Student.objects.get(id=sid)
        std = StudentForm(request.POST,instance=stddata)
        if (std.is_valid()):
            std.save()
            return redirect('/display')#redirecting to the root path
    else:
        stddata = Student.objects.get(id=sid)
        stdform= StudentForm(instance=stddata)
        return render(request,'EditStudent.html',{'data':stdform})
'''Destroy Student 
Edit Student'''
# Create your views here.
