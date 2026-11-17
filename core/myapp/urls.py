from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.student_api, name="student_api"),
    path("<int:id>/", views.student_delete, name="student_delete"),
    path("<int:id>/update/", views.student_update, name="student_update"),
]
