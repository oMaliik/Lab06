from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    id = models.CharField(max_length=50 ,unique=True,primary_key=True)
    courses = models.ManyToManyField(Course, related_name='students')
