"""Crea o actualiza el superusuario 'admin' durante el build de Vercel.

La contraseña se toma de la variable de entorno DJANGO_SUPERUSER_PASSWORD.
Se ejecuta en cada deploy: si el usuario ya existe, solo sincroniza la
contraseña con la variable.
"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if not password:
    print('AVISO: DJANGO_SUPERUSER_PASSWORD no esta definida; no se crea el admin')
else:
    user, created = User.objects.get_or_create(
        username='admin',
        defaults={'email': 'admin@example.com'},
    )
    user.is_staff = True
    user.is_superuser = True
    user.set_password(password)
    user.save()
    print('Superusuario admin', 'creado' if created else 'actualizado')
