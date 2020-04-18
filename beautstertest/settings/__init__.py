from decouple import config

phase = config('PHASE', default='dev', cast=str)

if phase == 'dev':
    from beautstertest.settings import dev
elif phase == 'prod':
    from beautstertest.settings import prod
