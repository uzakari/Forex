from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('payment/', views.payment_stripe, name='payment'),
    path('weather/', views.weather, name='weather'),
    path('post/', views.BlogPost, name='post')

]
