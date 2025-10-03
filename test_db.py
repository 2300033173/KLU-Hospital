#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
django.setup()

from django.db import connection
from django.contrib.auth.models import User

def test_database():
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Database connection successful: {result}")
        
        # Test user count
        user_count = User.objects.count()
        print(f"✅ Users in database: {user_count}")
        
        # Show database info
        db_name = connection.settings_dict['NAME']
        db_engine = connection.settings_dict['ENGINE']
        print(f"✅ Database: {db_engine}")
        print(f"✅ Database name: {db_name}")
        
    except Exception as e:
        print(f"❌ Database error: {e}")

if __name__ == '__main__':
    test_database()