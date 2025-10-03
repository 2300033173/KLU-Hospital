#!/usr/bin/env python
import os
import sys
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
    django.setup()
    
    from django.core.management import execute_from_command_line
    
    print("Setting up Hospital Management System...")
    
    # Run migrations
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create users
    print("Creating users...")
    execute_from_command_line(['manage.py', 'setup_users'])
    
    print("Setup complete!")