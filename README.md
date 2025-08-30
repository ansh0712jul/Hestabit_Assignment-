# 🏥 Hestabit Healthcare  

A **Healthcare Management System** built with **Django 5**, **Django REST Framework (DRF)**, **JWT Authentication**, and **Jinja2 Templates**.  
It provides both **web pages (Jinja)** and **REST APIs** for managing patients, doctors, and patient–doctor mappings.  

---

## 🚀 Features  

- 🔐 **Authentication & Authorization**  
  - User registration & JWT-based login.  
  - Access-protected APIs using `Bearer` tokens.  

- 👩‍⚕️ **Doctors**  
  - Publicly accessible list of doctors.  
  - Create, update, and delete (JWT protected).  

- 🧑‍🤝‍🧑 **Patients**  
  - Full CRUD (JWT protected).  
  - Each patient is linked with doctors through mappings.  

- 🔗 **Mappings**  
  - Manage doctor–patient relationships.  
  - Filter mappings by patient.  

- 🎨 **Frontend Templates (Jinja2)**  
  - `/doctors/` → doctor listing.  
  - `/patients/` → patient listing.  

---

## ⚙️ Installation & Local Setup  

Clone the repository and follow the steps:  

```bash
# 1) Create virtual environment
python -m venv .venv

# 2) Activate environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Setup environment variables
cp .env.example .env
# Edit SECRET_KEY and optionally DATABASE_URL (for Postgres)

# 5) Apply migrations
python manage.py migrate

# 6) (Optional) Create superuser
python manage.py createsuperuser

# 7) Run development server
python manage.py runserver

```
---

-Now visit: http://127.0.0.1:8000/


## 🔑 Authentication & API Endpoints  

### Auth  

**Register**  
`POST /api/auth/register/`  

**Login**  
`POST /api/auth/login/`  
```json
{
  "username": "alice@example.com",
  "password": "Secret123!"
}
```
### Authorization Header



Authorization: Bearer <access>
## Patients (JWT Protected)

- **GET** `/api/patients/` → list patients  
- **POST** `/api/patients/` → create patient  
- **GET** `/api/patients/{id}/` → retrieve patient  
- **PUT** `/api/patients/{id}/` → update patient  
- **DELETE** `/api/patients/{id}/` → delete patient  

---

## Doctors

- **GET** `/api/doctors/` → public list  
- **POST** `/api/doctors/` → add doctor (JWT)  
- **PUT** `/api/doctors/{id}/` → update doctor (JWT)  
- **DELETE** `/api/doctors/{id}/` → delete doctor (JWT)  

---

## Mappings (JWT Protected)

- **GET** `/api/mappings/` → list mappings  
- **GET** `/api/mappings/by-patient/{patient_id}/` → mappings for a specific patient  
- **POST** `/api/mappings/` → create mapping  
- **DELETE** `/api/mappings/{id}/` → remove mapping  


## 🗂️ Data Modeling  
Here’s an overview of the ER Diagram / Data Model used in the project:  

📸 **Add your screenshot(s) below**  

---

## 📌 Tech Stack  

- **Backend**: Django 5, Django REST Framework  
- **Auth**: JWT (`djangorestframework-simplejwt`)  
- **Frontend**: Jinja2 templates  
- **Database**: SQLite (default), PostgreSQL (optional via `DATABASE_URL`)  

---

## 🛠️ Future Improvements  

- Role-based access (Admin, Doctor, Patient)  
- Appointment scheduling system  
- Email notifications & reminders  
- API rate limiting & caching for scalability  

---

## 🤝 Contributing  

Contributions, issues, and feature requests are welcome!  
Feel free to open a **PR** or report a bug.  

---

## 📄 License  

This project is licensed under the **MIT License**.  
