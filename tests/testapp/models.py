from django.test import TestCase
from django.db import models
from versionfield import VersionField


class DummyModel(models.Model):
    version = VersionField()


class DummyModelCustomBit(models.Model):
    version = VersionField(number_bits=(8, 16, 8))
