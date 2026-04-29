# Healthcare Patient API

A HIPAA-compliant REST API for managing patient records,
appointments, and medical history.

## Features
- Patient registration and profile management
- Appointment scheduling and reminders
- Medical record storage and retrieval
- Role-based access (Doctor, Nurse, Admin, Patient)
- Audit logging for all data access

## Tech Stack
- Django 2.2 (REST API backend)
- PostgreSQL (Patient data storage)
- Celery + Redis (Async tasks)
- JWT Authentication

## Security Compliance
- HIPAA data handling requirements
- All API endpoints require authentication
- Patient data encrypted at rest
- CI/CD security scanning via CI/CD ThreatIntel

## Installation
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
