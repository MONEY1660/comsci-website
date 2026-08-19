from django.contrib import admin
from .models import Student, major, Student1, Student3, Student4

@admin.register(Student)
class StdentsAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'prefix_name', 'first_name', 'last_name')
    

@admin.register(major)
class majorAdmin(admin.ModelAdmin):
    list_display = ('mj_name',)

@admin.register(Student1)
class Student1Admin(admin.ModelAdmin):
    list_display = ('st_id', 'prefix_name', 'first_name', 'last_name')

@admin.register(Student3)
class Student3Admin(admin.ModelAdmin):
    list_display = ('st_id', 'prefix_name', 'first_name', 'last_name')

@admin.register(Student4)
class Student4Admin(admin.ModelAdmin):
    list_display = ('st_id', 'prefix_name', 'first_name', 'last_name')
