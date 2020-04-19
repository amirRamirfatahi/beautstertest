from decouple import config

from beautstertest.settings.base import *


phase = config('PHASE', default='dev', cast=str)

if phase == 'dev':
    from beautstertest.settings.dev import *
elif phase == 'prod':
    from beautstertest.settings.prod import *
elif phase == 'test':
    from beautstertest.settings.test import *
