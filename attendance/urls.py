from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.home, name='home'),
    path('subject/<int:id>/', views.subject_students, name='subject_students'),
    path('submit-attendance/<int:id>/', views.submit_attendance, name='submit_attendance'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-student/', views.add_student, name='add_student'),
]
