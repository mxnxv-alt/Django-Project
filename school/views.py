from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.template import loader
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SubjectForm, AttendanceForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Subject, Attendance, CustomUser

class UserRegisterView(CreateView):
    try:
        form_class = CustomUserCreationForm
        success_url = reverse_lazy("login")
        template_name = "registration/signup.html"
    except Exception as e:
        print(e)

def main(request):
    template = loader.get_template('main.html')
    if request.user.is_authenticated:
        print('yes the user is logged-in')
    else:
        print('no the user is not logged-in')
    return HttpResponse(template.render({}, request))

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = request.user
            attendance.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'attendances'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'TEACHER':
            return Attendance.objects.all()
        elif user.role == 'STUDENT':
            return Attendance.objects.filter(student=user)
        else:
            return Attendance.objects.none()

@login_required
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject/add_subject.html', {'form': form})

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'TEACHER':
            return Subject.objects.filter(teacher=user)
        elif user.role == 'STUDENT':
            return user.enrolled_subjects.all()
        else:
            return Subject.objects.none()
