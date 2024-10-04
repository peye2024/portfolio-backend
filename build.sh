#!/usr/bin/env bash

set -o errexit  # exit on error

# Install required packages
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create superuser non-interactively
python manage.py shell <<EOF
from django.contrib.auth.models import User

username = 'shimul'
email = 'hasaanshimul@gmail.com'
password = 'BitFactory61'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
EOF
