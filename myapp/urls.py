from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
    path('students/<int:student_id>/', views.student_details, name='student_details'),
]
