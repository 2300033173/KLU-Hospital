#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
django.setup()

from django.contrib.auth.models import User, Group
from hospital.models import Doctor, Patient

def create_admin():
    """Create admin user"""
    try:
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'first_name': 'Admin',
                'last_name': 'User',
                'email': 'admin@hospital.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        admin_user.set_password('admin123')
        admin_user.save()
        
        admin_group, _ = Group.objects.get_or_create(name='ADMIN')
        admin_user.groups.add(admin_group)
        
        print(f"[OK] Admin created: username='admin', password='admin123'")
        return admin_user
    except Exception as e:
        print(f"[ERROR] Error creating admin: {e}")

def create_doctors():
    """Create all doctors from the login file"""
    doctors_data = [
        {'username': 'Cardiologist', 'password': 'Cardiologist', 'first_name': 'Dr. Cardio', 'last_name': 'Specialist', 'department': 'Cardiologist'},
        {'username': 'Dermatologist', 'password': 'Dermatologist', 'first_name': 'Dr. Derma', 'last_name': 'Specialist', 'department': 'Dermatologists'},
        {'username': 'EMS', 'password': 'EMS', 'first_name': 'Dr. Emergency', 'last_name': 'Specialist', 'department': 'Emergency Medicine Specialists'},
        {'username': 'Allergist', 'password': 'Allergist', 'first_name': 'Dr. Allergy', 'last_name': 'Specialist', 'department': 'Allergists/Immunologists'},
        {'username': 'Anesthesiologist', 'password': 'Anesthesiologist', 'first_name': 'Dr. Anesthesia', 'last_name': 'Specialist', 'department': 'Anesthesiologists'},
        {'username': 'CRS', 'password': 'CRS', 'first_name': 'Dr. Colon', 'last_name': 'Surgeon', 'department': 'Colon and Rectal Surgeons'},
    ]
    
    doctor_group, _ = Group.objects.get_or_create(name='DOCTOR')
    
    for doc_data in doctors_data:
        try:
            # Create or get user
            user, created = User.objects.get_or_create(
                username=doc_data['username'],
                defaults={
                    'first_name': doc_data['first_name'],
                    'last_name': doc_data['last_name'],
                    'email': f"{doc_data['username'].lower()}@hospital.com"
                }
            )
            user.set_password(doc_data['password'])
            user.save()
            user.groups.add(doctor_group)
            
            # Create or get doctor profile
            doctor, created = Doctor.objects.get_or_create(
                user=user,
                defaults={
                    'department': doc_data['department'],
                    'address': 'Hospital Address',
                    'mobile': '1234567890',
                    'status': True  # Pre-approved
                }
            )
            
            print(f"[OK] Doctor created: username='{doc_data['username']}', password='{doc_data['password']}', department='{doc_data['department']}'")
            
        except Exception as e:
            print(f"[ERROR] Error creating doctor {doc_data['username']}: {e}")

def create_sample_patients():
    """Create sample patients"""
    patients_data = [
        {'username': 'patient1', 'password': 'patient123', 'first_name': 'John', 'last_name': 'Doe', 'symptoms': 'Fever and headache'},
        {'username': 'patient2', 'password': 'patient123', 'first_name': 'Jane', 'last_name': 'Smith', 'symptoms': 'Back pain'},
        {'username': 'patient3', 'password': 'patient123', 'first_name': 'Bob', 'last_name': 'Johnson', 'symptoms': 'Chest pain'},
    ]
    
    patient_group, _ = Group.objects.get_or_create(name='PATIENT')
    
    for pat_data in patients_data:
        try:
            # Create or get user
            user, created = User.objects.get_or_create(
                username=pat_data['username'],
                defaults={
                    'first_name': pat_data['first_name'],
                    'last_name': pat_data['last_name'],
                    'email': f"{pat_data['username']}@email.com"
                }
            )
            user.set_password(pat_data['password'])
            user.save()
            user.groups.add(patient_group)
            
            # Create or get patient profile
            patient, created = Patient.objects.get_or_create(
                user=user,
                defaults={
                    'symptoms': pat_data['symptoms'],
                    'address': 'Patient Address',
                    'mobile': '9876543210',
                    'assignedDoctorId': 1,  # Assign to first doctor
                    'status': True  # Pre-approved
                }
            )
            
            print(f"[OK] Patient created: username='{pat_data['username']}', password='{pat_data['password']}', symptoms='{pat_data['symptoms']}'")
            
        except Exception as e:
            print(f"[ERROR] Error creating patient {pat_data['username']}: {e}")

if __name__ == '__main__':
    print("Creating Hospital Management System Users...")
    print("=" * 50)
    
    # Create admin
    create_admin()
    print()
    
    # Create doctors
    print("Creating Doctors...")
    create_doctors()
    print()
    
    # Create patients
    print("Creating Sample Patients...")
    create_sample_patients()
    print()
    
    print("=" * 50)
    print("All users created successfully!")
    print("\nLOGIN CREDENTIALS:")
    print("ADMIN: username='admin', password='admin123'")
    print("DOCTORS: username=department_name, password=department_name")
    print("PATIENTS: username='patient1/2/3', password='patient123'")