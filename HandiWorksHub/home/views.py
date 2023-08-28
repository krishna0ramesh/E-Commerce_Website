from django.shortcuts import render
from django.http import HttpResponse
from .models import items,ceramics
# Create your views here.
def home(request):
    return render(request,'home.html')
def shop(request):
    item_dict={
        'item_key':items.objects.all()
    }
    return render(request,'shop.html',item_dict)
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
def ceramic(request):
    ceramic_dict={
        'ceramic_key':ceramics.objects.all()
    }
    return render(request,'ceramic.html',ceramic_dict)
def planter(request):
    return render(request,'planter.html')
def candle(request):
    return render(request,'candle.html')
def card(request):
    return render(request,'card.html')