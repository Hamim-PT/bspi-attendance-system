from django.contrib import admin
from .models import Subject, Student, Attendance, SessionalMark

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(SessionalMark)
