from django.shortcuts import render
from students.models import Student

def index(request):
    students = Student.objects.all().order_by("std_id")
    return render(request, "index.html", {"students": students})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
