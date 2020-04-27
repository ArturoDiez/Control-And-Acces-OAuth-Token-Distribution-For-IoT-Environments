from django.apps import AppConfig

import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

class ServicioiotConfig(AppConfig):
    name = 'ServicioIoT'
