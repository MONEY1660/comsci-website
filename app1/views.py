from datetime import date

from django.shortcuts import render

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

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)

    context={
        "student": student,
    }

    return render(request, 'student_detail.html', context)

    