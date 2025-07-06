from pathlib import Path
import os  # Por si necesitas usar os.path.join en algún momento

# 📁 Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Clave secreta (¡no la subas a producción así!)
SECRET_KEY = 'django-insecure-_e)u421oh-$z&=p)n647w!-3clj9l(3b921wf^jfbv*dbk*$*@'

# 🐞 Modo debug solo para desarrollo
DEBUG = True

# 🌐 Hosts permitidos (vacío en desarrollo, pero obligatorio en producción)
ALLOWED_HOSTS = []

# 🧩 Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps de terceros
    'django_extensions',
    'widget_tweaks',

    # Tu app
    'core',
]

# 🧱 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 Configuración de URLs
ROOT_URLCONF = 'cuenta_c.urls'

# 🎨 Configuración de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'core' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 WSGI
WSGI_APPLICATION = 'cuenta_c.wsgi.application'

# 🗃️ Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internacionalización
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 🖼️ Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 📸 Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 📬 Email (solo consola en desarrollo)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'cffferic@gmail.com'

# 🆔 Campo por defecto para modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔐 Redirecciones de login/logout
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/auth/home/'
LOGOUT_REDIRECT_URL = '/auth/login/'
