from django.shortcuts import render
from apps.doctors.models import Doctor
from apps.patients.models import Patient

def home(request):
    ctx = {
        "doctor_count": Doctor.objects.count(),
        "patient_count": Patient.objects.count(),
    }
    return render(request, "website/index.html", ctx)

def doctors_page(request):
    return render(request, "website/doctors.html", {"doctors": Doctor.objects.all()})

def patients_page(request):
    return render(request, "website/patients.html", {"patients": Patient.objects.select_related("created_by").all()})
