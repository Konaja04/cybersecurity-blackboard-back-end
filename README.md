# Backend Django (login con SQLite)

Backend de autenticación para el clon de Blackboard. Guarda los usuarios en
SQLite con la contraseña **hasheada** (PBKDF2) usando el sistema de usuarios de
Django.

## Levantar el backend

Desde la carpeta raíz del proyecto (`blackboard-clone/`):

```bash
source backend_venv/bin/activate      # activa el entorno virtual
cd backend
python manage.py runserver 8000
```

El backend queda en `http://127.0.0.1:8000`.

## Endpoints

| Método | URL              | Body JSON                          | Descripción                  |
|--------|------------------|------------------------------------|------------------------------|
| POST   | `/api/register/` | `{"username": "...", "password":...}` | Crea un usuario nuevo        |
| POST   | `/api/login/`    | `{"username": "...", "password":...}` | Valida credenciales          |
| POST   | `/api/logout/`   | —                                  | Cierra la sesión             |

### Crear un usuario de prueba

```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alumno01","password":"miClave123"}'
```

Luego puedes iniciar sesión desde el formulario de React.

## Ver / administrar usuarios

Crea un superusuario y entra al admin de Django en `http://127.0.0.1:8000/admin/`:

```bash
python manage.py createsuperuser
```

## Notas

- La base de datos es `backend/db.sqlite3`.
- Las contraseñas **nunca** se guardan en texto plano; se almacenan hasheadas.
- CORS está configurado para el dev server de Vite (`http://localhost:5173`).
- `DEBUG=True` y el `SECRET_KEY` por defecto son solo para desarrollo local.
