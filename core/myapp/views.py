from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student

# Converts and validates student data.
from .serializers import StudentSerializers


# Create your views here.
@api_view(["GET", "POST"])
def student_api(request):

    if request.method == "GET":
        student = Student.objects.all()
        # This converts multiple Student objects into a serialized representation.
        serializer = StudentSerializers(student, many=True)
        # converted student data back to the frontend
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
