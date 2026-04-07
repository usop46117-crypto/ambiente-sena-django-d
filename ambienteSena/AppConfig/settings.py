"""
Django settings for AmbienteSena project.
Actualizado para despliegue en Render + MySQL (Clever Cloud)
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno del archivo .env
load_dotenv()

# RUTA PARA LAS IMAGENES DE LOS ELEMENTOS
RUTA_IMAGENES_ELEMENTOS = BASE_DIR / 'AmbienteSena' / 'Public' / 'Img' / 'elementos'

# --- CONFIGURACIÓN DE SEGURIDAD ---

# Se usa la clave del .env o una por defecto para desarrollo
SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-kj7l)0lu4&65=8u0m#vsh+vt#kc7lipc+i0a$_4-zx#sq7$#0g')

# DEBUG se apaga automáticamente si no estás en local
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Configuración de Hosts permitidos (Incluye Render)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '10.3.129.163', '.onrender.com']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# --- DEFINICIÓN DE APLICACIONES ---

INSTALLED_APPS = [
    'AmbienteSena',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware para estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AmbienteSena.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'AmbienteSena' / 'Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AmbienteSena.wsgi.application'


# --- BASE DE DATOS (MYSQL - CLEVER CLOUD) ---

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# --- VALIDACIÓN DE CONTRASEÑAS ---

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- INTERNACIONALIZACIÓN ---

LANGUAGE_CODE = 'es-co' # Cambiado a español
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True


# --- ARCHIVOS ESTÁTICOS (CSS, JS, IMAGES) ---

STATIC_URL = '/static/'

# Directorio donde están tus archivos estáticos en desarrollo
STATICFILES_DIRS = [
    BASE_DIR / 'AmbienteSena' / 'Public'
]

# Directorio donde se recopilarán para producción
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de almacenamiento para producción (WhiteNoise)
if not DEBUG:
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'