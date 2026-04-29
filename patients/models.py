"""
Patient data models for Healthcare API.
Handles patient records, appointments, and medical history.
"""

class Patient:
    """Core patient record model"""
    patient_id: str
    full_name: str
    date_of_birth: str
    blood_type: str
    emergency_contact: str
    insurance_number: str


class Appointment:
    """Medical appointment scheduling"""
    appointment_id: str
    patient_id: str
    doctor_id: str
    appointment_date: str
    appointment_type: str  # checkup, emergency, followup
    status: str  # scheduled, completed, cancelled
    notes: str


class MedicalRecord:
    """Patient medical history records"""
    record_id: str
    patient_id: str
    diagnosis: str
    prescription: str
    created_by: str
    created_at: str
