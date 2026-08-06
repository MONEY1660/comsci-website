from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('std_id', 'prefix', 'fname', 'lname')
    search_fields = ('std_id', 'fname', 'lname')
    list_filter = ('prefix',)
