from django.contrib import admin
from .models import *
#Register your models here.
admin.site.register(items)
admin.site.register(ceramics)
admin.site.register(planters)
admin.site.register(candles)
admin.site.register(cards)

class orderAdmin(admin.ModelAdmin):
    list_display=('recipient','phno','email','item_name','uid','num','bookedOn')
admin.site.register(orders,orderAdmin)