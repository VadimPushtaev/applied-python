from datetime import timedelta, datetime
from unittest import TestCase

from limit import Limit
from resource import Resource


class ResourceTestCase(TestCase):
    def setUp(self):
        self._resource = Resource('test', [
            Limit(1, timedelta(seconds=1)),
            Limit(2, timedelta(seconds=1)),
        ])

    def test_can_consume(self):
        resource = self._resource

        dt = datetime(2018, 1, 1)
        self.assertTrue(resource.can_consume(dt))
        self.assertFalse(resource.can_consume(dt, 2))
        self.assertTrue(resource.can_consume(dt, 1))

    def test_consume(self):
        resource = self._resource

        dt = datetime(2018, 1, 1)
        resource.consume(dt)
        with self.assertRaises(RuntimeError):
            resource.consume(dt)
        resource.consume(dt + timedelta(seconds=1))
