import datetime

from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def index(malumot):
    projects = Project.objects.all()
    servis = Service.objects.all()
    blog = Blog.objects.all()
    return render(malumot,'index.html',{"project":projects,"servis":servis,"blog":blog})

def about(malumot):
    ishchilar = Worker.objects.all()
    return render(malumot,'about.html',{"workers":ishchilar})



def blog(malumot):
    blog = Blog.objects.all()
    return render(malumot,'blog.html',{"blog":blog})

def contact(malumot):
    if malumot.method=="POST":
        ismi = malumot.POST.get('ism')
        familyasi = malumot.POST.get('fam')
        emaili = malumot.POST.get('mail')
        matni = malumot.POST.get('text')
        vaqt = datetime.datetime.now()
        Messages(name=ismi,last_name=familyasi,email=emaili,text=matni,date=vaqt).save()
    contact = Contact.objects.all()
    return render(malumot,"contact.html",{"contact":contact})

def servis(malumot):
    servis = Service.objects.all()
    return render(malumot,'services.html',{"servis":servis})



def projects(malumot):
    loyihalar = Project.objects.all()
    return render(malumot,'project.html',{"project":loyihalar})

def single(malumot):
    return render(malumot,'single.html')






