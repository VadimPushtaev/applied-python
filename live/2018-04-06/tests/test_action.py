from datetime import timedelta, datetime

from action import Action
from tests import BaseTestCase


class ActionTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self._action = Action('test', [
            (2, self._resource1),
            (3, self._resource2),
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

