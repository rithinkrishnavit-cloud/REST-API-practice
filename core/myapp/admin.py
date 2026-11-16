from django.contrib import admin
from .models import Student


# Register your models here.
class StudentCustom(admin.ModelAdmin):
    list_display = ("name", "age", "course", "place")
    ordering = ("id",)


admin.site.register(Student, StudentCustom)
