from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "gender", "created_by", "created_at")
    search_fields = ("name", "created_by__username")
    list_filter = ("gender", "created_at")
