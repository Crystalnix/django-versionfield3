#!/usr/bin/env python

import sys

try:
    import django
except ImportError:
    print("Error: missing test dependency:")
    print("  django library is needed to run test suite")
    print("  you can install it with 'pip install django'")
    sys.exit(1)

from django.conf import settings


def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests.

    settings.configure(
        INSTALLED_APPS=[
            'versionfield',
        ],
        DATABASE_ENGINE='django.db.backends.sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        DEBUG=True,
        TEMPLATE_DEBUG=True,
    )

    if django.VERSION[:2] >= (1, 7):
        django.setup()

    apps = ['versionfield']

    from django.test.utils import get_runner

    DjangoTestRunner = get_runner(settings)

    failures = DjangoTestRunner(verbosity=2, interactive=True).run_tests(apps)
    sys.exit(failures)


if __name__ == '__main__':
    main()
