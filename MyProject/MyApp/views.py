from django.shortcuts import render
from .models import Person
from .form import PersonForm
from django.http import HttpResponse

def Home(request):
    '''name=input("Enter your name :")
    n1=int(input("Entr your number 1:"))
    n2=int(input("Entr your number 2:"))
    li=['abc',123,76.8,'xyz']'''
    return render(request,'HomePage.html')
#Home()
def About(request):
    return render(request,'AboutUs.html')
def ShowData(request):
    data=Person.objects.all()
    return render(request,"ShowPerson.html",{'data':data})
def loadPerson(request):
    perform=PersonForm()
    return render(request,'PersonForm.html',{'personData':perform})

