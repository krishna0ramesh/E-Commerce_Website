from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('shop/', views.shop,name='shop'),
    path('pages', views.pages),
    path('contact/', views.contact,name='contact'),
    path('shoppingcart/', views.shoppingcart,name='shoppingcart'),
    path('checkout/', views.checkout,name='checkout'),
    path('ceramic/', views.ceramic,name='ceramic'),
    path('planter/', views.planter,name='planter'),
    path('candle/', views.candle,name='candle'),
    path('card/', views.card,name='card'),

]
