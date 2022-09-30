from django.db import models

# Create your models here.
CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),

)
CHOICES2 = (
    ("cse", "CSE"),
    ("ec", "EC"),
    ("ee", "EE"),
    ("me", "ME"),
    ("ce", "CE"),

)


class data1(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    branch = models.CharField(choices=CHOICES2, max_length=100, default='---')
    year = models.CharField(choices=CHOICES, max_length=100, default='---')


class ADM(models.Model):
    adname = models.CharField(max_length=100)
    adpass = models.CharField(max_length=100, default=0000)
    mdses = models.CharField(max_length=100)