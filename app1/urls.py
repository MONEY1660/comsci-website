from django.urls import path
from . import views


app_name = 'app1'


urlpatterns = [

    # ==============================
    # หน้าเว็บไซต์หลัก
    # ==============================

    path(
        '',
        views.index,
        name='home'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),


    # ==============================
    # ข้อมูลนักศึกษาทั้ง 4 ชั้นปี
    # ==============================

    path(
        'students/',
        views.students,
        name='students'
    ),


    # ==============================
    # รายละเอียดนักศึกษาปี 1
    # ==============================

    path(
        'student1/<str:pk>/',
        views.student_detail1,
        name='student_detail1'
    ),


    # ==============================
    # รายละเอียดนักศึกษาปี 2
    # ==============================

    path(
        'student/<str:pk>/',
        views.student_detail2,
        name='student_detail2'
    ),


    # ==============================
    # รายละเอียดนักศึกษาปี 3
    # ==============================

    path(
        'student3/<str:pk>/',
        views.student_detail3,
        name='student_detail3'
    ),


    # ==============================
    # รายละเอียดนักศึกษาปี 4
    # ==============================

    path(
        'student4/<str:pk>/',
        views.student_detail4,
        name='student_detail4'
    ),
]