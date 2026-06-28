from django.shortcuts import render, redirect,get_object_or_404
from datetime import date
import requests
from .models import Subject, Student, Attendance, SessionalMark


def home(request):
    subjects = Subject.objects.all()
    return render(request, 'home.html', {'subjects': subjects})
def landing(request):
    return render(request, 'landing.html')


def subject_students(request, id):
    subject = Subject.objects.get(id=id)
    students = Student.objects.filter(subject=subject)
    return render(request, 'students.html', {
        'students': students,
        'subject': subject
    })


def submit_attendance(request, id):
    subject = Subject.objects.get(id=id)
    students = Student.objects.filter(subject=subject)
    today = date.today()

    for student in students:
        status = request.POST.get(str(student.id))
        is_present = True if status == 'on' else False

        Attendance.objects.update_or_create(
            student=student,
            date=today,
            defaults={'is_present': is_present}
        )

        if is_present:
            send_sms(student.phone)

    return redirect('subject_students', id=id)


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    # total present days count
    present_days = Attendance.objects.filter(
        student=student,
        is_present=True
    ).count()

    # sessional marks
    mark, _ = SessionalMark.objects.get_or_create(student=student)

    if request.method == 'POST':
        mark.marks = request.POST.get('marks')
        mark.save()
        return redirect('student_detail', id=student.id)

    return render(request, 'student_detail.html', {
        'student': student,
        'present_days': present_days,
        'mark': mark,
    })

def send_sms(phone):
    pass
def add_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Subject.objects.create(name=name)
            return redirect('home')
    return render(request, 'add_subject.html')


def add_student(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        subject_id = request.POST.get('subject')
        subject = Subject.objects.get(id=subject_id)
        if name and phone and subject:
            Student.objects.create(name=name, phone=phone, subject=subject)
            return redirect('home')
    return render(request, 'add_student.html', {'subjects': subjects})