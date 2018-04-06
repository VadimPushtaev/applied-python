from datetime import timedelta, datetime
from unittest import TestCase

from limit import Limit


class LimitTestCase(TestCase):
    def setUp(self):
        self._limit = Limit(2, timedelta(seconds=3))

    def test_can_consume(self):
        limit = self._limit

        dt = datetime(2018, 1, 1)
        self.assertTrue(limit.can_consume(dt))
        self.assertTrue(limit.can_consume(dt + timedelta(seconds=1), 2))
        self.assertFalse(limit.can_consume(dt + timedelta(seconds=2), 4))
        self.assertTrue(limit.can_consume(dt + timedelta(seconds=3), 1))

    def test_consume(self):
        limit = self._limit

        dt = datetime(2018, 1, 1)
        limit.consume(dt)
        limit.consume(dt + timedelta(seconds=1), 1)
        with self.assertRaises(RuntimeError):
            limit.consume(dt + timedelta(seconds=2), 1)
