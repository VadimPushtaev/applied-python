import unittest
from command_handler.message import MessageCommandHandler


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = MessageCommandHandler()
        for i in range(5):
            self.obj.handle('_start yeah' + str(i))

    def test_string(self):
        self.assertEqual('yeah4', self.obj.handle('_get'))


if __name__ == '__main__':
    unittest.main()
