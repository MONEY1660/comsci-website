from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('study-plans/', views.study_plans, name='study_plans'),
    path('teachers/', views.teachers, name='teachers'),
]
