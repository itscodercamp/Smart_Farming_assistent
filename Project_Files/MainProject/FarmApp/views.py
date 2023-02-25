from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from Products.models import *
from Category.models import *
# views.py

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def Contact(request):

    if request.method == "POST":
        dd = Contact_Form_Entry_Records()
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('subjects')

        dd.firstname = firstname
        dd.lastname = lastname
        dd.email = email
        dd.subject = message
        dd.save()
        
        messages.success(request,"Successfully submited your details to our team we'll contact you Soon ")
        return redirect('Contact')
    return render(request,'contact.html')


def BasicFarming(request):
    data = Flower_farming.objects.all()
    content = {
        'basic_farming':data
    }
    
    return render(request,'basicfarming.html',content)


def Eq_Farming(request):
    data =Farming_Equpments.objects.all()
    content = {
        'basic_farming':data
    }
    return render(request,'Eq.html',content)



def ProductFraming(request):
    data = Farming_Product.objects.all()
    data1 = Farming_Product_List.objects.all()
    content = {
        
        'basic_farming':data,
        'basic_farming1':data1
    }
    return render(request,'pro.html',content)
    
def Schemes(nothing):
    return render(nothing,'scheme.html')

# types of farming section starts here 

def GuideFarming(request):
    data = Types_Of_Farming.objects.all()
    content = {
        'basic_farming':data
    }
    return render(request,'Type.html',content)

def Full_Details(request,slug):
    data = Types_Of_Farming.objects.get(slug=slug)
    content = {
        'basic_farming':data
    }
    return render(request,'fulldet.html',content)


def search(request):

    return render(request, 'buyingdetails.html' )