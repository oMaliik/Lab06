from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'id']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
