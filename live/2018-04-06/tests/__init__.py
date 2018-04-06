from datetime import timedelta
from unittest import TestCase

from limit import Limit
from resource import Resource


class BaseTestCase(TestCase):
    def setUp(self):
        self._resource1 = Resource('test_resource1', [
            Limit(2, timedelta(seconds=1)),
            Limit(3, timedelta(seconds=1)),
        ])
        self._resource2 = Resource('test_resource2', [
            Limit(6, timedelta(seconds=1)),
            Limit(7, timedelta(seconds=1)),
        ])
        self._resource3 = Resource('test_resource3', [
            Limit(10, timedelta(seconds=1)),
            Limit(10, timedelta(seconds=1)),
        ])
