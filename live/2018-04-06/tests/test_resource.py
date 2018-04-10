from datetime import timedelta, datetime

from tests import BaseTestCase


class ResourceTestCase(BaseTestCase):
    def test_can_consume(self):
        resource = self._resource1

        dt = datetime(2018, 1, 1)
        self.assertTrue(resource.can_consume(dt))
        self.assertFalse(resource.can_consume(dt, 3))
        self.assertTrue(resource.can_consume(dt, 2))

    def test_consume(self):
        resource = self._resource1

        dt = datetime(2018, 1, 1)
        resource.consume(dt)
        with self.assertRaises(RuntimeError):
            resource.consume(dt, 2)
        resource.consume(dt + timedelta(seconds=1), 2)
