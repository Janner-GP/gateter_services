"""
WSGI config for gateter_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.getenv("ENVIROMENT") == "local":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gateter_app.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gateter_app.settings.prod')

application = get_wsgi_application()
