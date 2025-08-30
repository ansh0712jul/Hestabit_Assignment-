from rest_framework import serializers
from .models import PatientDoctorMapping

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ["id", "patient", "doctor", "assigned_at"]
        read_only_fields = ["id", "assigned_at"]
