"""
Django settings for Portal_EDU project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm_q+suutz60_lslh5dy38chvx&#d1v5p(#bxbc8m9o!dmwope('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'academic_calendars',
    'assignments',
    'assists',
    'authentication',
    'blood_types',
    'classrooms',
    'contact_types',
    'courses',
    'entrance_schedules',
    'extra_curricular_activities',
    'extra_curricular_activity_types',
    'genres',
    'grade_names',
    'grades',
    'incharge_appointments',
    'incharge_contacts',
    'incharge_types',
    'incharges',
    'levels',
    'medical_backgrounds',
    'modules',
    'notes',
    'planification_types',
    'planifications',
    'schedules',
    'schools',
    'sections',
    'staff_activities',
    'staff_contacts',
    'staff_appointments',
    'staff_entrance_reports',
    'staff_entrance_schedules',
    'staff_meeting_schedules',
    'staff_types',
    'staffs',
    'student_contacts',
    'student_control_list',
    'student_reports',
    'students',
    'subjects',
    'tasks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Portal_EDU.urls'

WSGI_APPLICATION = 'Portal_EDU.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'apolodb' ,
        'USER': 'adminDuM2sPH' ,
        'PASSWORD': 'q_cAnvJHLXB7',
        'HOST': '127.0.0.1',
        'PORT': '3307'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-gt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = (

   os.path.join(BASE_DIR, "static"),
)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = 'apolodb_login'
LOGOUT_URL = 'apolodb_logout'


