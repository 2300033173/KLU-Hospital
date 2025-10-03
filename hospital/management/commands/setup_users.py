from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from hospital.models import Doctor, Patient

class Command(BaseCommand):
    help = 'Create initial users for hospital management system'

    def handle(self, *args, **options):
        self.stdout.write('Creating Hospital Management System Users...')
        
        # Create admin
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
        self.stdout.write('[OK] Admin created: admin/admin123')

        # Create doctors
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
            
            doctor, created = Doctor.objects.get_or_create(
                user=user,
                defaults={
                    'department': doc_data['department'],
                    'address': 'Hospital Address',
                    'mobile': '1234567890',
                    'status': True
                }
            )
            self.stdout.write(f'[OK] Doctor created: {doc_data["username"]}/{doc_data["password"]}')

        # Create patients
        patients_data = [
            {'username': 'patient1', 'password': 'patient123', 'first_name': 'John', 'last_name': 'Doe', 'symptoms': 'Fever and headache'},
            {'username': 'patient2', 'password': 'patient123', 'first_name': 'Jane', 'last_name': 'Smith', 'symptoms': 'Back pain'},
            {'username': 'patient3', 'password': 'patient123', 'first_name': 'Bob', 'last_name': 'Johnson', 'symptoms': 'Chest pain'},
        ]
        
        patient_group, _ = Group.objects.get_or_create(name='PATIENT')
        
        for pat_data in patients_data:
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
            
            # Get first doctor for assignment
            first_doctor = Doctor.objects.first()
            doctor_id = first_doctor.user.id if first_doctor else 1
            
            patient, created = Patient.objects.get_or_create(
                user=user,
                defaults={
                    'symptoms': pat_data['symptoms'],
                    'address': 'Patient Address',
                    'mobile': '9876543210',
                    'assignedDoctorId': doctor_id,
                    'status': True
                }
            )
            self.stdout.write(f'[OK] Patient created: {pat_data["username"]}/{pat_data["password"]}')

        self.stdout.write(self.style.SUCCESS('All users created successfully!'))