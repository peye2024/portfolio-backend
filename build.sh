#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create superuser non-interactively
echo "from django.contrib.auth.models import User; \
if not User.objects.filter(username='shimul').exists(): \
    User.objects.create_superuser('shimul', 'hasaanshimul@gmail.com', 'BitFactory61')" | python manage.py shell
