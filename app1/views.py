from datetime import date

from django.shortcuts import render, get_object_or_404

from .models import (
    Student,
    Student1,
    Student3,
    Student4,
)


# =========================================================
# HOME
# =========================================================

def index(request):

    context = {
        'title': 'สาขาวิชาวิทยาการคอมพิวเตอร์',
        'date': date.today(),
    }

    return render(
        request,
        'home.html',
        context
    )


# =========================================================
# DASHBOARD
# =========================================================

def dashboard(request):

    context = {
        'title': 'Home Page',
        'date': date.today(),
        'students': Student.objects.all(),
    }

    return render(
        request,
        'index.html',
        context
    )


# =========================================================
# ABOUT
# =========================================================

def about(request):

    context = {
        'title': 'About Page',
        'date': date.today(),
        'students': Student.objects.all(),
    }

    return render(
        request,
        'about.html',
        context
    )


# =========================================================
# CONTACT
# =========================================================

def contact(request):

    context = {
        'title': 'Contact Page',
        'date': date.today(),
        'students': Student.objects.all(),
    }

    return render(
        request,
        'contact.html',
        context
    )


# =========================================================
# ฟังก์ชันเรียงนักศึกษา
# เรียงจากเลข 2 ตัวท้ายของ st_id
# =========================================================

def sort_students(student_queryset):

    students = list(student_queryset)

    students.sort(
        key=lambda student: (
            int(student.st_id[-2:])
            if student.st_id
            and student.st_id[-2:].isdigit()
            else 999,
            student.st_id or '',
        )
    )

    return students


# =========================================================
# ข้อมูลนักศึกษาทั้ง 4 ชั้นปี
# =========================================================

def students(request):

    student1_list = sort_students(
        Student1.objects.all()
    )

    student2_list = sort_students(
        Student.objects.all()
    )

    student3_list = sort_students(
        Student3.objects.all()
    )

    student4_list = sort_students(
        Student4.objects.all()
    )

    context = {

        # ปี 1
        'student1_list': student1_list,

        # ปี 2
        'student2_list': student2_list,

        # ปี 3
        'student3_list': student3_list,

        # ปี 4
        'student4_list': student4_list,

        'title': 'ข้อมูลนักศึกษา',
    }

    return render(
        request,
        'student.html',
        context
    )


# =========================================================
# ฟังก์ชันกลางสำหรับหน้า Detail
# =========================================================

def student_detail_by_model(
    request,
    model,
    pk,
    year,
    detail_url_name
):

    # -----------------------------------------
    # นักศึกษาคนปัจจุบัน
    # -----------------------------------------

    student = get_object_or_404(
        model,
        st_id=pk
    )


    # -----------------------------------------
    # ดึงนักศึกษาของชั้นปีนั้นทั้งหมด
    # -----------------------------------------

    student_list = sort_students(
        model.objects.all()
    )


    # -----------------------------------------
    # หาตำแหน่งนักศึกษาคนปัจจุบัน
    # -----------------------------------------

    current_index = next(
        (
            index
            for index, item in enumerate(student_list)
            if item.st_id == student.st_id
        ),
        None
    )


    # -----------------------------------------
    # ค่าเริ่มต้น
    # -----------------------------------------

    prev_student = None
    next_student = None


    # -----------------------------------------
    # นักศึกษาคนก่อนหน้า
    # -----------------------------------------

    if (
        current_index is not None
        and current_index > 0
    ):

        prev_student = (
            student_list[current_index - 1]
        )


    # -----------------------------------------
    # นักศึกษาคนถัดไป
    # -----------------------------------------

    if (
        current_index is not None
        and current_index < len(student_list) - 1
    ):

        next_student = (
            student_list[current_index + 1]
        )


    # -----------------------------------------
    # ส่งข้อมูลให้ student_detail.html
    # -----------------------------------------

    context = {

        'student': student,

        'prev_student': prev_student,

        'next_student': next_student,

        'year': year,

        'detail_url_name': detail_url_name,

        'current_number': (
            current_index + 1
            if current_index is not None
            else 0
        ),

        'student_count': len(student_list),
    }


    return render(
        request,
        'student_detail.html',
        context
    )


# =========================================================
# DETAIL : ปี 1
# =========================================================

def student_detail1(request, pk):

    return student_detail_by_model(
        request=request,
        model=Student1,
        pk=pk,
        year=1,
        detail_url_name='app1:student_detail1'
    )


# =========================================================
# DETAIL : ปี 2
# =========================================================

def student_detail2(request, pk):

    return student_detail_by_model(
        request=request,
        model=Student,
        pk=pk,
        year=2,
        detail_url_name='app1:student_detail2'
    )


# =========================================================
# DETAIL : ปี 3
# =========================================================

def student_detail3(request, pk):

    return student_detail_by_model(
        request=request,
        model=Student3,
        pk=pk,
        year=3,
        detail_url_name='app1:student_detail3'
    )


# =========================================================
# DETAIL : ปี 4
# =========================================================

def student_detail4(request, pk):

    return student_detail_by_model(
        request=request,
        model=Student4,
        pk=pk,
        year=4,
        detail_url_name='app1:student_detail4'
    )