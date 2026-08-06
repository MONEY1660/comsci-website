from django.db import models


class Student(models.Model):
    PREFIX_CHOICES = [
        ('นาย', 'นาย'),
        ('น.ส.', 'น.ส.'),
        ('นาง', 'นาง'),
    ]

    std_id = models.CharField(max_length=20, unique=True)
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.std_id} {self.prefix} {self.fname} {self.lname}"
