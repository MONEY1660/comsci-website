from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# st_id,prefix_name,first_name,last_name
class Student(models.Model):
    PREFIX_CHOICES = [
        ('นาย', 'นาย'),
        ('นาง', 'นาง'),
        ('นางสาว', 'นางสาว'),
    ]

    st_id = models.CharField(max_length=10, primary_key=True)
    prefix_name = models.CharField(max_length=20, choices=PREFIX_CHOICES, blank=True, default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prefix_name} {self.first_name} {self.last_name}".strip()

    def get_full_name(self):
        return f"{self.prefix_name} {self.first_name} {self.last_name}".strip()
