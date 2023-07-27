from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home),
    path('shop/', views.shop),
    path('pages', views.pages),
    path('contact/', views.contact),
]