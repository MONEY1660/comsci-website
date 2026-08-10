from django.urls import path 
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
]
