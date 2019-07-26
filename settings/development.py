from .base import *

# import raven
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demoga',
        'USER': 'root',
        'PASSWORD': os.environ["PASSWORD"],
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
            'NAME': 'demoga_db_test',
        }
    },
}


RAVEN_CONFIG = {}
