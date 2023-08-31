from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import items,ceramics,planters,candles,cards
from .form import orderform

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
    if request.method=='POST':
        form=orderform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=orderform()
    dict_form={
        'form':form
    }
    return render(request,'contact.html',dict_form)
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
    planter_dict={
        'planter_key':planters.objects.all()
    }
    return render(request,'planter.html',planter_dict)
def candle(request):
    candle_dict={
        'candle_key':candles.objects.all()
    }
    return render(request,'candle.html',candle_dict)
def card(request):
    card_dict={
        'card_key':cards.objects.all()
    }
    return render(request,'card.html',card_dict)
