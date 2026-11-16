# Think of it like a translator.
# - Django Model → JSON
# - JSON → Django Model

from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
