from datetime import date

from django.shortcuts import render, get_object_or_404

from .models import Student


def index(request):
    context = {
        'title': 'สาขาวิชาวิทยาการคอมพิวเตอร์',
        'date': date.today(),
    }

    return render(request, 'home.html', context)


def dashboard(request):
    """The original student-records dashboard, kept available separately."""

    context = {
        'title': 'Home Page',
        'date': date.today(),
        'students': Student.objects.all(),
    }

    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About Page',
        'date': date.today(),
        'students': Student.objects.all(),
    }

    return render(request, 'about.html', context)


def contact(request):
    context = {
        'title': 'Contact Page',
        'date': date.today(),
        'students': Student.objects.all(),
    }

    return render(request, 'contact.html', context)


# ==============================
# Student List
# ==============================

def students(request):

    student_list = Student.objects.all().order_by('st_id')

    context = {
        'students': student_list,
        'title': 'ข้อมูลนักศึกษา',
    }

    return render(
        request,
        'student.html',
        context
    )


# ==============================
# Student Detail
# ==============================

def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    context = {
        'student': student,
    }

    return render(
        request,
        'student_detail.html',
        context
    )
