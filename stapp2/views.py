from django.shortcuts import render
from students.models import Student
from .models import Course, StudyPlan, Teacher

def index(request):
    students = Student.objects.all().order_by("std_id")
    # Get some featured content for the homepage
    featured_courses = Course.objects.all()[:3]  # Show 3 featured courses
    featured_teachers = Teacher.objects.all()[:3]  # Show 3 featured teachers

    context = {
        "students": students,
        "featured_courses": featured_courses,
        "featured_teachers": featured_teachers,
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    course_list = Course.objects.all()
    return render(request, 'courses.html', {'courses': course_list})


def study_plans(request):
    study_plan_list = StudyPlan.objects.all()
    return render(request, 'study_plans.html', {'study_plans': study_plan_list})


def teachers(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teacher_list})
