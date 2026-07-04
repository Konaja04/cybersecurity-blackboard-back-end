import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Student


def _parse_body(request):
    """Lee el JSON enviado por el frontend de React."""
    try:
        return json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return {}


@csrf_exempt
def register(request):
    """Crea un usuario (contraseña HASHEADA) y un Student asociado."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    data = _parse_body(request)
    username = (data.get('username') or '').strip()
    password = data.get('password') or ''

    if not username or not password:
        return JsonResponse(
            {'error': 'Usuario y contraseña son obligatorios'}, status=400
        )

    student, _ = Student.objects.get_or_create(
        nombre=username,
        defaults={'contra': password},
    )

    return JsonResponse(
        {
            'ok': True,
            'message': 'Usuario creado'
        },
        status=201,
    )


@csrf_exempt
def login_view(request):
    """Valida las credenciales contra la base de datos."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    data = _parse_body(request)
    username = (data.get('username') or '').strip()
    password = data.get('password') or ''

    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse(
            {'ok': False, 'error': 'Usuario o contraseña incorrectos'}, status=401
        )

    login(request, user)  # crea la sesión
    return JsonResponse({'ok': True, 'username': user.username})


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'ok': True})
