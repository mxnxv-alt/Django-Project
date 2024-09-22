from django.urls import path
from . import views
from .views import UserRegisterView, mark_attendance, AttendanceListView, add_subject, SubjectListView
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('mark_attendance/', mark_attendance, name='mark_attendance'),
    path('attendance_list/', AttendanceListView.as_view(), name='attendance_list'),
    path("", TemplateView.as_view(template_name="main.html"), name="main"), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_subject/', add_subject, name='add_subject'),
    path('subject_list/', SubjectListView.as_view(), name='subject_list'),
]