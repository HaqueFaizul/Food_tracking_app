from django.shortcuts import render,redirect
from .models import Student
def loadform(request):
    return render(request,'myform.html')
def displayform(request):
    #vname = request.GET['sname']
    #vname = request.POST['sname']
    vname = request.POST.get('sname')
    vgender=request.POST.get('gender')
    vlanguage=request.POST.getlist('language')
    vsubject=request.POST.get('subject')
    return render(request,'displayForm.html',{'name':vname,'gender':vgender,'language':vlanguage,'Subject':vsubject})
def loadStudentForm(request):
    return render(request, 'studentform.html')
def insertStudent(request):
    if request.method=='POST':
        vname=request.POST.get('sname')
        vroll = request.POST.get('sroll')
        vadd = request.POST.get('sadd')
        vgender=request.POST.get('gender')
        vlanguage = request.POST.getlist('language')
        vcountry = request.POST.get('country')
        std=Student()
        std.name=vname
        std.roll_number=vroll
        std.address=vadd
        std.gender=vgender
        std.language=vlanguage
        std.country=vcountry
        std.save()
        return redirect('/show')
    else:
        return render(request, 'studentform.html')
def displayStudent(request):
    std=Student.objects.all()
    return render(request,'ShowStudent.html',{'student':std})
def deleteStudent(request,sid):
    std=Student.objects.get(id=sid)
    std.delete()
    return redirect('/show')
def editStudent(request,sid):
    std=Student.objects.get(id=sid)
    return render(request,'editStudent.html',{'data':std})

def updateStudent(request,sid):
    std = Student.objects.get(id=sid)
    vname = request.POST.get('sname')
    vroll = request.POST.get('sroll')
    vadd = request.POST.get('sadd')
    vgender = request.POST.get('gender')
    vlanguage = request.POST.getlist('language')
    std.name = vname
    std.roll_number = vroll
    std.address = vadd
    std.gender = vgender
    std.language = vlanguage
    std.save()
    return redirect('/show')
def studentstatus(request,sid,status):
    if status=='ACTIVE':
        std=Student.objects.get(id=sid)
        std.status='INACTIVE'
        std.save()
        return redirect('/show')
    else:
        std = Student.objects.get(id=sid)
        std.status = 'ACTIVE'
        std.save()
        return redirect('/show')






