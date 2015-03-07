INSTALLED_APPS = (
    "testapp",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = "django_tests_secret_key"
