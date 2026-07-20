from datetime import date

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home Page',
        'date': date.today(),
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About Page',
        'date': date.today(),
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'title': 'Contact Page',
        'date': date.today(),
    }
    return render(request, 'contact.html', context)
