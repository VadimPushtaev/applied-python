from command_handler.sample import SampleCommandHandler
from unittest import TestCase


class SampleCommandHandlerTestCase(TestCase):
    def setUp(self):
        print(SampleCommandHandler)
        self._handler = SampleCommandHandler()

    def test_handle(self):
        self.assertEqual('_test', self._handler.handle('_test'))
        self.assertIsNone(self._handler.handle('test'))
        with self.assertRaises(RuntimeError):
            self._handler.handle('@test')
