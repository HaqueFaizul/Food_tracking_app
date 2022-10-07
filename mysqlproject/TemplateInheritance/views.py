from django.shortcuts import render

# Create your views here.

def loadPage(request):
    return render(request,'ChildPage.html')
#Parentpage,Childpage

def loadIndex(request):
    return render(request,'Index.html')