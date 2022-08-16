from dataclasses import fields
from my_app.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields ='__all__'
   