Hestabit Healthcare — Django 5 + DRF + JWT + Jinja2

Run locally
1) python -m venv .venv
   - Windows: .venv\\Scripts\\activate
   - macOS/Linux: source .venv/bin/activate
2) pip install -r requirements.txt
3) cp .env.example .env  (edit SECRET_KEY; optionally set DATABASE_URL for Postgres)
4) python manage.py migrate
5) python manage.py createsuperuser  # optional
6) python manage.py runserver
7) Visit http://127.0.0.1:8000/  (Jinja pages)
   - /doctors/ and /patients/ render lists using templates

Auth + API
- POST /api/auth/register/   {"name":"Alice","email":"alice@example.com","password":"Secret123!"}
- POST /api/auth/login/      {"username":"alice@example.com","password":"Secret123!"} -> {access, refresh}
- Use header: Authorization: Bearer <access>
- Patients (JWT): GET/POST /api/patients/, GET/PUT/DELETE /api/patients/{id}/
- Doctors: GET /api/doctors/ (public), modify with JWT
- Mappings (JWT): GET /api/mappings/, GET /api/mappings/by-patient/{patient_id}/, POST /api/mappings/, DELETE /api/mappings/{id}/
