from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.IntegerField()
    # Assuming this relates to a major/program
    # We could add a foreign key to major from app1 if needed

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        verbose_name_plural = "Courses"

class StudyPlan(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration_years = models.IntegerField()
    # Could have a many-to-many relationship with courses
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Study Plans"

class Teacher(models.Model):
    PREFIX_CHOICES = [
        ('อาจารย์', 'อาจารย์'),
        ('ผู้ช่วยศาสตราจารย์', 'ผู้ช่วยศาสตราจารย์'),
        ('รองศาสตราจารย์', 'รองศาสตราจารย์'),
        ('ศาสตราจารย์', 'ศาสตราจารย์'),
    ]

    prefix = models.CharField(max_length=20, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    # Could add specialty/field, bio, etc.
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return f"{self.prefix} {self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.prefix} {self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Teachers"