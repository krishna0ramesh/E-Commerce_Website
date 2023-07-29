from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def shop(request):
    return render(request,'shop.html')
def pages(request):
    options={'opt':['shopping cart','checkout page']
        
             }
    return render(request,'pages.html',options)
def contact(request):
    details={
        'number':987654321,
        'email':'handiworkshub@gmail.com',
    }
    return render(request,'contact.html',details)
def shoppingcart(request):
    return render(request,'shoppingcart.html')
def checkout(request):
    return render(request,'checkout.html')