from django.shortcuts import render
from .models import Country,State


def loadIndex(request):
    cntry=Country.objects.all()
    #state=State.objects.all()
    return render(request,'IndexPage.html',{'country':cntry})
def getState(request):
    vcountry=request.GET.get('country')
    state=State.objects.filter(country=vcountry)
    return render(request,'getState.html',{'state':state})

# Create your views here.
