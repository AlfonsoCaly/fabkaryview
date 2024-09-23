from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('weddings/', views.weddings, name='weddings'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('family/', views.family, name='family'),
    path('contact/', views.contact, name='contact'), 
]