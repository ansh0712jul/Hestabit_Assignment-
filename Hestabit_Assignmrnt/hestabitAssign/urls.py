from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.website.views import home, doctors_page, patients_page

urlpatterns = [
    path("admin/", admin.site.urls),

    # Jinja pages
    path("", home, name="home"),
    path("doctors/", doctors_page, name="doctors_page"),
    path("patients/", patients_page, name="patients_page"),

    # APIs
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/patients/", include("apps.patients.urls")),
    path("api/doctors/", include("apps.doctors.urls")),
    path("api/mappings/", include("apps.mappings.urls")),
]
