from .base import *

# import raven
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newga',
        'USER': 'root',
        'PASSWORD': 'gGJGsy834ghsjdXDCGsjdfgaXD',
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
            'NAME': 'eaf_db_test',
        }
    },
}


RAVEN_CONFIG = {}
