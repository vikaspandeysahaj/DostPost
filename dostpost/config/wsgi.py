"""
WSGI config for dostpost project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from config.config_loader import dostpost_config

dostpost_config.load_settings()

application = get_wsgi_application()
