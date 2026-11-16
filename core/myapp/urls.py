from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.student_api, name="student_api"),
]
