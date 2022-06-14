finally/client/                                                                                     000755  000765  000024  00000000000 14234617076 016176  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/docker-compose.yml                                                                          000644  000765  000024  00000001315 14234576354 020360  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         version: '3.5'

services:
  webapp:
    build:
      context: ${PWD}/client
      dockerfile: ${PWD}/client/Dockerfile

  db:
    image: postgres:12
    environment:
      - POSTGRES_DB=finallydb
      - POSTGRES_USER=finally
      - POSTGRES_PASSWORD=finally
      - PGDATA=/var/lib/postgresql/data/pgdata
    restart: unless-stopped

  api:
    depends_on:
      - db
    build:
      context: ${PWD}/server
      dockerfile: ${PWD}/server/Dockerfile
    volumes:
      - "${PWD}/server:/app"
    ports:
      - 8000:8000
    command: >
      sh -c "cd finally_api && python manage.py makemigrations && python manage.py makemigrations --merge && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
                                                                                                                                                                                                                                                                                                                   finally/server/                                                                                     000755  000765  000024  00000000000 14234555746 016233  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/requirements.txt                                                                     000644  000765  000024  00000000167 14234600063 021502  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         Django>=4.0.4,<4.1.0
djangorestframework>=3.13.1,<3.14.0
psycopg2-binary>=2.9.3,<3.0.0
drf-spectacular>=0.22.1,<0.23.0
                                                                                                                                                                                                                                                                                                                                                                                                         finally/server/Dockerfile                                                                           000644  000765  000024  00000000422 14234552071 020207  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         FROM python:3.10-alpine

# Remove buffer from docker
ENV PYTHONUNBUFFERED 1

# Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Define workdir
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D finally
USER finally
                                                                                                                                                                                                                                              finally/server/finally_api/                                                                         000755  000765  000024  00000000000 14234554014 020505  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/gpa/                                                                     000755  000765  000024  00000000000 14234575153 021263  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/manage.py                                                                000755  000765  000024  00000001233 14234552545 022320  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         #!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finally_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
                                                                                                                                                                                                                                                                                                                                                                     finally/server/finally_api/finally_api/                                                             000755  000765  000024  00000000000 14234553162 022777  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/finally_api/asgi.py                                                      000644  000765  000024  00000000617 14234552545 024304  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         """
ASGI config for finally_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finally_api.settings')

application = get_asgi_application()
                                                                                                                 finally/server/finally_api/finally_api/__init__.py                                                  000644  000765  000024  00000000000 14234552545 025102  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/finally_api/__pycache__/                                                 000755  000765  000024  00000000000 14234600645 025206  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/finally_api/settings.py                                                  000644  000765  000024  00000007720 14234600540 025210  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         """
Django settings for finally_api project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-o5k=+922-%usq+0irhn2dl$4qfx4-y^@9962k_u6=p^p%c4bz!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'drf_spectacular',
    "gpa.apps.GpaConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "finally_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "finally_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME", "finallydb"),
        "USER": os.environ.get("DB_USER", "finally"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "finally"),
        "HOST": os.environ.get("DB_HOST", "db"),
        "PORT": os.environ.get("DB_PORT", 5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Rest Apis
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Finally API',
    'DESCRIPTION': 'Finally description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
                                                finally/server/finally_api/finally_api/urls.py                                                      000644  000765  000024  00000002216 14234600645 024336  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         """finally_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from gpa.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += router.urls
                                                                                                                                                                                                                                                                                                                                                                                  finally/server/finally_api/finally_api/wsgi.py                                                      000644  000765  000024  00000000617 14234552545 024332  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         """
WSGI config for finally_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finally_api.settings')

application = get_wsgi_application()
                                                                                                                 finally/server/finally_api/finally_api/__pycache__/settings.cpython-310.pyc                         000644  000765  000024  00000005546 14234600540 031553  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    `sb�  �                
   @   s   d Z ddlZddlmZ ee��� jjZdZdZ	g Z
g d�Zg d�ZdZd	g dd
g d�id�gZdZddej�dd�ej�dd�ej�dd�ej�dd�ej�dd�d�iZddiddiddiddigZdgd d!d"�Zd#d$d%d&d'�Zd(Zd)ZdZdZd*Zd+ZdS ),a0  
Django settings for finally_api project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
�    N)�PathzBdjango-insecure-o5k=+922-%usq+0irhn2dl$4qfx4-y^@9962k_u6=p^p%c4bz!T)	zdjango.contrib.adminzdjango.contrib.authzdjango.contrib.contenttypeszdjango.contrib.sessionszdjango.contrib.messageszdjango.contrib.staticfilesZrest_frameworkZdrf_spectacularzgpa.apps.GpaConfig)z-django.middleware.security.SecurityMiddlewarez4django.contrib.sessions.middleware.SessionMiddlewarez)django.middleware.common.CommonMiddlewarez)django.middleware.csrf.CsrfViewMiddlewarez7django.contrib.auth.middleware.AuthenticationMiddlewarez4django.contrib.messages.middleware.MessageMiddlewarez6django.middleware.clickjacking.XFrameOptionsMiddlewarezfinally_api.urlsz/django.template.backends.django.DjangoTemplatesZcontext_processors)z(django.template.context_processors.debugz*django.template.context_processors.requestz+django.contrib.auth.context_processors.authz3django.contrib.messages.context_processors.messages)�BACKENDZDIRS�APP_DIRS�OPTIONSzfinally_api.wsgi.application�defaultz&django.db.backends.postgresql_psycopg2ZDB_NAMEZ	finallydbZDB_USER�finallyZDB_PASSWORDZDB_HOST�dbZDB_PORTi8  )�ENGINE�NAME�USER�PASSWORD�HOST�PORTr
   zHdjango.contrib.auth.password_validation.UserAttributeSimilarityValidatorz>django.contrib.auth.password_validation.MinimumLengthValidatorz?django.contrib.auth.password_validation.CommonPasswordValidatorz@django.contrib.auth.password_validation.NumericPasswordValidatorz1rest_framework.authentication.BasicAuthentication)z*rest_framework.permissions.IsAuthenticatedz"drf_spectacular.openapi.AutoSchema)ZDEFAULT_AUTHENTICATION_CLASSESZDEFAULT_PERMISSION_CLASSESZDEFAULT_SCHEMA_CLASSzFinally APIzFinally descriptionz1.0.0F)ZTITLEZDESCRIPTION�VERSIONZSERVE_INCLUDE_SCHEMAzen-usZUTCzstatic/zdjango.db.models.BigAutoField)�__doc__�os�pathlibr   �__file__�resolve�parentZBASE_DIR�
SECRET_KEY�DEBUG�ALLOWED_HOSTS�INSTALLED_APPS�
MIDDLEWARE�ROOT_URLCONF�	TEMPLATES�WSGI_APPLICATION�environ�get�	DATABASES�AUTH_PASSWORD_VALIDATORSZREST_FRAMEWORKZSPECTACULAR_SETTINGS�LANGUAGE_CODE�	TIME_ZONE�USE_I18N�USE_TZ�
STATIC_URL�DEFAULT_AUTO_FIELD� r(   r(   �(/app/finally_api/finally_api/settings.py�<module>   sh    
������������	�                                                                                                                                                          finally/server/finally_api/finally_api/__pycache__/urls.cpython-310.pyc                             000644  000765  000024  00000002345 14234600645 030700  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �sb�  �                   @   s�   d Z ddlmZ ddlmZ ddlmZmZmZ ddl	m
Z
 edejj�ede�� dd	�ed
ejdd�dd	�edejdd�dd	�gZee
j7 ZdS )at  finally_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
�    )�admin)�path)�SpectacularAPIView�SpectacularRedocView�SpectacularSwaggerView)�routerzadmin/zapi/schema/�schema)�namezapi/schema/swagger-ui/)�url_namez
swagger-ui� ZredocN)�__doc__Zdjango.contribr   �django.urlsr   Zdrf_spectacular.viewsr   r   r   Zgpa.routersr   �site�urls�as_view�urlpatterns� r   r   �$/app/finally_api/finally_api/urls.py�<module>   s    �                                                                                                                                                                                                                                                                                           finally/server/finally_api/finally_api/__pycache__/wsgi.cpython-310.pyc                             000644  000765  000024  00000001040 14234557320 030654  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    e�rb�  �                   @   s0   d Z ddlZddlmZ ej�dd� e� ZdS )z�
WSGI config for finally_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
�    N)�get_wsgi_application�DJANGO_SETTINGS_MODULEzfinally_api.settings)�__doc__�os�django.core.wsgir   �environ�
setdefault�application� r
   r
   �$/app/finally_api/finally_api/wsgi.py�<module>   s
    	
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                finally/server/finally_api/finally_api/__pycache__/__init__.cpython-310.pyc                         000644  000765  000024  00000000205 14234553162 031444  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    e�rb    �                   @   s   d S )N� r   r   r   �(/app/finally_api/finally_api/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                               finally/server/finally_api/gpa/migrations/                                                          000755  000765  000024  00000000000 14234576360 023440  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/gpa/models.py                                                            000644  000765  000024  00000002615 14234602210 023105  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from decimal import Decimal
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models, transaction


# Create your models here.
class Account(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")

    def account_number(self):
        return str(self.id).zfill(12)


class Transaction(models.Model):
    CREDIT = 'CREDIT'
    DEBIT = 'DEBIT'
    TRANSACTION_TYPES = ((CREDIT, CREDIT), (DEBIT, DEBIT))

    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    note = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")

    def _update_account_balance(self) -> None:
        if self.transaction_type == self.DEBIT:
            self.amount *= -1

        self.account_id.current_balance += self.amount

    @transaction.atomic
    def save(self, *args, **kwargs):
        self._update_account_balance()
        super(Transaction, self).save(*args, **kwargs)
        self.account_id.save()
                                                                                                                   finally/server/finally_api/gpa/viewsets.py                                                          000644  000765  000024  00000004201 14234613445 023500  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Sum

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from gpa.models import Account, Transaction
from gpa.serializers import AccountSerializer, TransactionSerializer, UserSerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    perimssion_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Account.objects.filter(user_id=self.request.user)

    def get_permmissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=True, url_path="date/(?P<date>[^/.]+)", methods=["GET"])
    def date(self, request, pk, date):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            _date = datetime.strptime(date, "%Y%m%d")
            account = Account.objects.get(pk=pk)
            total_amount = account.transactions.filter(date__gte=_date).aggregate(Sum('amount'))['amount__sum']
            previous_balance = account.current_balance + total_amount

            res = AccountSerializer(account).data
            res['current_balance'] = previous_balance
            return Response(res)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    perimssion_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Transaction.objects.filter(user_id=self.request.user)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permmission_classes = [IsAdminUser]
    queryset = User.objects.all()
                                                                                                                                                                                                                                                                                                                                                                                               finally/server/finally_api/gpa/serializers.py                                                       000644  000765  000024  00000001173 14234602360 024162  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from gpa.models import Account, Transaction


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(ModelSerializer):
    account_number = SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_account_number(self, instance):
        return instance.account_number()


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
                                                                                                                                                                                                                                                                                                                                                                                                     finally/server/finally_api/gpa/__init__.py                                                          000644  000765  000024  00000000000 14234554014 023353  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/gpa/__pycache__/                                                         000755  000765  000024  00000000000 14234613446 023471  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/gpa/apps.py                                                              000644  000765  000024  00000000212 14234554014 022564  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from django.apps import AppConfig


class GpaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gpa'
                                                                                                                                                                                                                                                                                                                                                                                      finally/server/finally_api/gpa/admin.py                                                             000644  000765  000024  00000000077 14234554014 022722  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from django.contrib import admin

# Register your models here.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 finally/server/finally_api/gpa/tests.py                                                             000644  000765  000024  00000000074 14234554014 022771  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from django.test import TestCase

# Create your tests here.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    finally/server/finally_api/gpa/routers.py                                                           000644  000765  000024  00000000507 14234602342 023331  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from rest_framework.routers import SimpleRouter

from gpa import viewsets

router = SimpleRouter()
router.register(r'accounts', viewsets.AccountViewSet, basename="accounts")
router.register(r'transactions', viewsets.TransactionViewSet, basename="transactions")
router.register(r'users', viewsets.UserViewSet, basename="users")
                                                                                                                                                                                         finally/server/finally_api/gpa/views.py                                                             000644  000765  000024  00000000077 14234554014 022767  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         from django.shortcuts import render

# Create your views here.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 finally/server/finally_api/gpa/__pycache__/viewsets.cpython-310.pyc                                 000644  000765  000024  00000005150 14234613446 030044  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    %sb�  �                   @   s�   d dl m Z  d dlmZ d dlmZ d dlmZ d dlmZ d dl	m
Z
 d dlmZmZ d dlmZ d d	lmZmZ d d
lmZmZmZ G dd� de
�ZG dd� de
�ZG dd� de
�ZdS )�    )�datetime)�User)�Sum��status)�action)�ModelViewSet)�IsAuthenticated�IsAdminUser)�Response)�Account�Transaction)�AccountSerializer�TransactionSerializer�UserSerializerc                   @   s>   e Zd ZeZegZdd� Zdd� Ze	dddgd�d	d
� �Z
dS )�AccountViewSetc                 C   �    | j jjrtjj| j jd�S d S �N)�user_id)�request�user�is_authenticatedr   �objects�filter��self� r   � /app/finally_api/gpa/viewsets.py�get_queryset   �   
�zAccountViewSet.get_querysetc                 C   s   | j dv r	t� gS t� gS )N)�list�retrieve)r   r	   r
   r   r   r   r   �get_permmissions   s   
zAccountViewSet.get_permmissionsTzdate/(?P<date>[^/.]+)�GET)�detail�url_path�methodsc           	      C   s�   |j js
ttjd�S z.t�|d�}tjj	|d�}|j
j|d��td��d }|j| }t|�j}||d< t|�W S  tjyH   ttjd� Y S  tyV   ttjd� Y S w )Nr   z%Y%m%d)�pk)Z	date__gte�amountZamount__sum�current_balance)r   r   r   r   �HTTP_401_UNAUTHORIZEDr   �strptimer   r   �get�transactionsr   �	aggregater   r)   r   �data�DoesNotExist�HTTP_404_NOT_FOUND�	Exception�HTTP_400_BAD_REQUEST)	r   r   r'   �dateZ_dateZaccountZtotal_amountZprevious_balance�resr   r   r   r4      s   


�zAccountViewSet.dateN)�__name__�
__module__�__qualname__r   �serializer_classr	   �perimssion_classesr   r"   r   r4   r   r   r   r   r      s    r   c                   @   s   e Zd ZeZegZdd� ZdS )�TransactionViewSetc                 C   r   r   )r   r   r   r   r   r   r   r   r   r   r   5   r   zTransactionViewSet.get_querysetN)r6   r7   r8   r   r9   r	   r:   r   r   r   r   r   r;   1   s    r;   c                   @   s    e Zd ZeZegZej�	� Z
dS )�UserViewSetN)r6   r7   r8   r   r9   r
   Zpermmission_classesr   r   �all�querysetr   r   r   r   r<   :   s    r<   N)r   �django.contrib.auth.modelsr   �django.db.modelsr   �rest_frameworkr   �rest_framework.decoratorsr   Zrest_framework.viewsetsr   Zrest_framework.permissionsr	   r
   �rest_framework.responser   Z
gpa.modelsr   r   Zgpa.serializersr   r   r   r   r;   r<   r   r   r   r   �<module>   s    !	                                                                                                                                                                                                                                                                                                                                                                                                                        finally/server/finally_api/gpa/__pycache__/routers.cpython-310.pyc                                  000644  000765  000024  00000000615 14234602343 027671  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �sbG  �                   @   sX   d dl mZ d dlmZ e� Zejdejdd� ejdejdd� ejdejdd� dS )�    )�SimpleRouter)�viewsets�accounts)�basename�transactions�usersN)	Zrest_framework.routersr   �gpar   �router�registerZAccountViewSetZTransactionViewSetZUserViewSet� r   r   �/app/finally_api/gpa/routers.py�<module>   s                                                                                                                       finally/server/finally_api/gpa/__pycache__/serializers.cpython-310.pyc                              000644  000765  000024  00000002650 14234602361 030523  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �sb{  �                   @   s`   d dl mZ d dlmZmZ d dlmZmZ G dd� de�ZG dd� de�Z	G dd	� d	e�Z
d
S )�    )�User)�ModelSerializer�SerializerMethodField)�Account�Transactionc                   @   �   e Zd ZG dd� d�ZdS )�UserSerializerc                   @   �   e Zd ZeZdZdS )zUserSerializer.Meta�__all__N)�__name__�
__module__�__qualname__r   �model�fields� r   r   �#/app/finally_api/gpa/serializers.py�Meta	   �    r   N�r   r   r   r   r   r   r   r   r      �    r   c                   @   s(   e Zd Ze� ZG dd� d�Zdd� ZdS )�AccountSerializerc                   @   r	   )zAccountSerializer.Metar
   N)r   r   r   r   r   r   r   r   r   r   r      r   r   c                 C   s   |� � S )N)�account_number)�self�instancer   r   r   �get_account_number   s   z$AccountSerializer.get_account_numberN)r   r   r   r   r   r   r   r   r   r   r   r      s    r   c                   @   r   )�TransactionSerializerc                   @   r	   )zTransactionSerializer.Metar
   N)r   r   r   r   r   r   r   r   r   r   r      r   r   Nr   r   r   r   r   r      r   r   N)�django.contrib.auth.modelsr   Zrest_framework.serializersr   r   �
gpa.modelsr   r   r   r   r   r   r   r   r   �<module>   s                                                                                            finally/server/finally_api/gpa/__pycache__/models.cpython-310.pyc                                   000644  000765  000024  00000003612 14234602224 027447  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �sb�  �                   @   s\   d dl mZ d dlmZ d dlmZ d dlmZmZ G dd� dej	�Z
G dd� dej	�Zd	S )
�    )�Decimal)�uuid4)�User)�models�transactionc                   @   sJ   e Zd Zejdedd�Zejdded�d�Z	ej
eejdd	�Zd
d� ZdS )�AccountTF)�primary_key�default�editable�
   �   r   ��
max_digits�decimal_placesr	   Zaccounts��	on_delete�related_namec                 C   s   t | j��d�S )N�   )�str�id�zfill��self� r   �/app/finally_api/gpa/models.py�account_number   s   zAccount.account_numberN)�__name__�
__module__�__qualname__r   �	UUIDFieldr   �
account_id�DecimalFieldr   �current_balance�
ForeignKeyr   �CASCADE�user_idr   r   r   r   r   r   	   s
    r   c                       s�   e Zd ZdZdZeefeeffZejdd�Zej	ded�Z
ej	dddd�Zejd	d
ed�d�Zejeejdd�Zddd�Zej� fdd��Z�  ZS )�Transaction�CREDIT�DEBITT)�auto_now_add�   )�
max_length�choices�2   )r+   �null�blankr   r   r   r   Ztransactionsr   �returnNc                 C   s0   | j | jkr|  jd9  _| j j| j7  _d S )N�����)�transaction_typer(   �amountr    r"   r   r   r   r   �_update_account_balance   s   z#Transaction._update_account_balancec                    s,   | � �  tt| �j|i |�� | j��  d S )N)r4   �superr&   �saver    )r   �args�kwargs��	__class__r   r   r6   #   s   zTransaction.save)r0   N)r   r   r   r'   r(   ZTRANSACTION_TYPESr   �DateTimeField�date�	CharFieldr2   Znoter!   r   r3   r#   r   r$   r    r4   r   �atomicr6   �__classcell__r   r   r9   r   r&      s    
r&   N)�decimalr   �uuidr   �django.contrib.auth.modelsr   �	django.dbr   r   �Modelr   r&   r   r   r   r   �<module>   s    	                                                                                                                      finally/server/finally_api/gpa/__pycache__/admin.cpython-310.pyc                                    000644  000765  000024  00000000246 14234557131 027262  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �rb?   �                   @   s   d dl mZ dS )�    )�adminN)Zdjango.contribr   � r   r   �/app/finally_api/gpa/admin.py�<module>   s                                                                                                                                                                                                                                                                                                                                                              finally/server/finally_api/gpa/__pycache__/apps.cpython-310.pyc                                     000644  000765  000024  00000000616 14234557114 027137  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �rb�   �                   @   s    d dl mZ G dd� de�ZdS )�    )�	AppConfigc                   @   s   e Zd ZdZdZdS )�	GpaConfigzdjango.db.models.BigAutoFieldZgpaN)�__name__�
__module__�__qualname__�default_auto_field�name� r	   r	   �/app/finally_api/gpa/apps.pyr      s    r   N)�django.appsr   r   r	   r	   r	   r
   �<module>   s                                                                                                                      finally/server/finally_api/gpa/__pycache__/__init__.cpython-310.pyc                                 000644  000765  000024  00000000175 14234557114 027733  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �rb    �                   @   s   d S )N� r   r   r   � /app/finally_api/gpa/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                                       finally/server/finally_api/gpa/migrations/__init__.py                                               000644  000765  000024  00000000000 14234554014 025527  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/gpa/migrations/__pycache__/                                              000755  000765  000024  00000000000 14234576361 025651  5                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         finally/server/finally_api/gpa/migrations/0001_initial.py                                           000644  000765  000024  00000003115 14234576360 026103  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         # Generated by Django 4.0.4 on 2022-05-04 22:23

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('current_balance', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(choices=[('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')], max_length=6)),
                ('note', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='gpa.account')),
            ],
        ),
    ]
                                                                                                                                                                                                                                                                                                                                                                                                                                                   finally/server/finally_api/gpa/migrations/__pycache__/0001_initial.cpython-310.pyc                  000644  000765  000024  00000002630 14234576361 032444  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    ��rbM  �                   @   sN   d dl mZ d dlmZ d dlmZmZ d dlZd dl	Z	G dd� dej
�Z
dS )�    )�Decimal)�settings)�
migrations�modelsNc                   @   s�   e Zd ZdZe�ej�gZej	dde
jejdddd�fde
jded�d	d
�fde
jejj
jjdejd�fgd�ej	dde
jddddd�fde
jdd�fde
jddgdd�fde
jdddd�fde
jded�d	d
�fde
jejj
jjddd�fgd�gZd S )!�	MigrationT�Account�
account_idF)�default�editable�primary_key�	serialize�current_balance�   �0�
   )�decimal_placesr	   �
max_digits�user_id�accounts)�	on_delete�related_name�to)�name�fields�Transaction�id�ID)�auto_createdr   r   �verbose_name�date)�auto_now_add�transaction_type)�CREDITr"   )�DEBITr#   �   )�choices�
max_length�note�2   )�blankr&   �null�amount�transactionszgpa.accountN)�__name__�
__module__�__qualname__�initialr   �swappable_dependencyr   �AUTH_USER_MODEL�dependencies�CreateModelr   �	UUIDField�uuid�uuid4�DecimalFieldr   �
ForeignKey�django�db�deletion�CASCADE�BigAutoField�DateTimeField�	CharField�
operations� rB   rB   �//app/finally_api/gpa/migrations/0001_initial.pyr   
   s,    
������r   )�decimalr   �django.confr   �	django.dbr   r   �django.db.models.deletionr:   r6   r   rB   rB   rB   rC   �<module>   s                                                                                                           finally/server/finally_api/gpa/migrations/__pycache__/__init__.cpython-310.pyc                      000644  000765  000024  00000000210 14234557131 032074  0                                                                                                    ustar 00victornatschke                  staff                           000000  000000                                                                                                                                                                         o
    �rb    �                   @   s   d S )N� r   r   r   �+/app/finally_api/gpa/migrations/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            