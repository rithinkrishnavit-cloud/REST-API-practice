from django.db.migrations import serializer
from django.shortcuts import render, get_object_or_404, redirect
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


# only allow delete request
@api_view(["DELETE"])
def student_delete(request, id):

    if request.method == "DELETE":
        student = get_object_or_404(Student, id=id)
        student.delete()
        # This sends a message back to the frontend.
        # dictionary
        return Response({"message": "Student deleted"})


@api_view(["PUT"])
def student_update(request, id):

    student = get_object_or_404(Student, id=id)

    serializer = StudentSerializers(student, data=request.data)

    if serializer.is_valid():
        serializer.save()
        # send updated data in frondend as json
        return Response(serializer.data)

    return Response(serializer.errors)


# Response() : takes that dictionary and sends it back as an API response, usually in JSON format.
