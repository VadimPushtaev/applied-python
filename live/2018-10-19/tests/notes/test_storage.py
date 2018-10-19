from notes.storage import MemoryStorage
from tests import BaseTestCase


class MemoryStorageTestCase(BaseTestCase):
    def test_get(self):
        storage = MemoryStorage()

        storage._data['x'] = 1

        self.assertEqual(1, storage.get('x'))
        self.assertIsNone(storage.get('y'))

    def test_set(self):
        storage = MemoryStorage()

        storage.set('x', 1)

        self.assertEqual(
            dict(x=1),
            storage._data
        )