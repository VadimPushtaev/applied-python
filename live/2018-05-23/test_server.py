import unittest

from server import process_batch


class ServerTestCase(unittest.TestCase):
    def test_process_batch(self):
        self.assertEqual([1, 8, 27], process_batch([1, 2, 3]))