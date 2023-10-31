from django.urls import path
from .import views
urlpatterns = [
    path('', views.hello, name='Students'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('add/', views.add, name='add'),

]