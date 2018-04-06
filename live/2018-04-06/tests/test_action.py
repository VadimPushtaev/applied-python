from datetime import timedelta, datetime
from unittest import TestCase

from action import Action
from limit import Limit
from resource import Resource


class ActionTestCase(TestCase):
    def setUp(self):
        self._action = Action('test', [
            Resource('test_resource1', [
                Limit(2, timedelta(seconds=1)),
                Limit(3, timedelta(seconds=1)),
            ]),
            Resource('test_resource2', [
                Limit(4, timedelta(seconds=1)),
                Limit(5, timedelta(seconds=1)),
            ]),
        ])

    def test_can_consume(self):
        action = self._action

        dt = datetime(2018, 1, 1)
        self.assertTrue(action.can_consume(dt))
        self.assertFalse(action.can_consume(dt, 3))
        self.assertTrue(action.can_consume(dt, 2))

    def test_consume(self):
        action = self._action

        dt = datetime(2018, 1, 1)
        action.consume(dt)
        with self.assertRaises(RuntimeError):
            action.consume(dt, 2)
        action.consume(dt, 1)

