from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import MappingSerializer

class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.select_related("patient", "doctor")
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"], url_path="by-patient/(?P<patient_id>[^/.]+)")
    def by_patient(self, request, patient_id=None):
        qs = self.get_queryset().filter(patient_id=patient_id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
