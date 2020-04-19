# Override default cache to use memcache for tests

CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
    }
}
