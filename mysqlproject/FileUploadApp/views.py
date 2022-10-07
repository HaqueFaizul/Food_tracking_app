from django.shortcuts import render,redirect
from .models import Book

def loadBookForm(request):
    return render(request,'BookForm.html')

def createBook(request):
    if request.method=='POST':
        vname=request.POST.get('bname')
        vauth = request.POST.get('bauth')
        vcpage = request.FILES['cpage']
        vebook = request.FILES['ebook']
        obj=Book()
        obj.Book_Name=vname
        obj.Book_author=vauth
        obj.Cover_page=vcpage
        obj.E_book=vebook
        obj.save()
        return redirect('/show')
def showbook(request):
    objbook=Book.objects.all()
    return render(request,'Booklist.html',{'book':objbook})

# Email handling
from django.core.mail import send_mail
from django.http import HttpResponse

def emailHandling(request):
    subject="Greetings"
    msg='Hi how are you..'
    to='deeparajkumar493@gmail.com'
    mail=send_mail(subject,msg,'haquefaizul92@gmail.com',['deeparajkumar493@gmail.com','dfwlekfk@'])

    if mail==1:
        return HttpResponse("Mail Send successfully")
    else:
        return HttpResponse('Mail not send')



