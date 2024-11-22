
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('service/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('myservice/', views.myservice, name='myservice'),
    path('appointment/', views.create_appointment, name='appointment'),
    path('contact/', views.contact, name = 'contact'),
    path('show/', views.show, name = 'show'),
    path('showcontact/', views.contactshow, name = 'showcontact'),
    path('delete/<int:id>', views.delete),
    path('deletecontact/<int:id>', views.deletecontact),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('departments/', views.departments, name='departments'),
    path('home/', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('asuccess/', views.asuccess, name='asuccess'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
]
