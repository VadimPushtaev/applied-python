from datetime import timedelta, datetime
from unittest import TestCase

from action import Action
from limit import Limit
from resource import Resource


class ActionTestCase(TestCase):
    def setUp(self):
        self._action = Action('test', [
            (
                2,
                Resource('test_resource1', [
                    Limit(2, timedelta(seconds=1)),
                    Limit(3, timedelta(seconds=1)),
                ]),
            ),
            (
                3,
                Resource('test_resource2', [
                    Limit(6, timedelta(seconds=1)),
                    Limit(7, timedelta(seconds=1)),
                ]),
            ),
        ])

    def test__can_consume(self):
        action = self._action

        dt = datetime(2018, 1, 1)
        self.assertTrue(action._can_consume(dt))
        action.consume(dt)
        self.assertFalse(action._can_consume(dt))
        self.assertTrue(action._can_consume(dt + timedelta(seconds=1)))

    def test_consume(self):
        action = self._action

        dt = datetime(2018, 1, 1)
        action.consume(dt)
        with self.assertRaises(RuntimeError):
            action.consume(dt)
        action.consume(dt + timedelta(seconds=1))

