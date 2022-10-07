from django.shortcuts import render
def SetCookie(request):
    #return render(request,'SetCookie.html')
    cookiedata=render(request,'SetCookie.html')# Cookie has been set
    cookiedata.set_cookie('data','Soujanya',max_age=3600)
    return cookiedata
def GetCookie(request):
    #mycookie=request.COOKIES['data']
    mycookie = request.COOKIES.get('data','No Data')
    return render(request,'GetCookie.html',{'data1':mycookie})
def DelCookie(request):
    cookiedata = render(request, 'delCookie.html')
    cookiedata.delete_cookie('data')
    return cookiedata
def SetSession(request):
    request.session['name']='Deepa'
    return render(request,'SetSession.html')

def GetSession(request):
    #sessiondata=request.session['name']
    sessiondata = request.session.get('name','None')
    return render(request,'GetSession.html',{'Data':sessiondata})

def DelSession(request):
    request.session.flush()
    return render(request,'DelSession.html')


