import unittest
from command_handler.message import MessageCommandHandler


class MyTestCase(unittest.TestCase):

    def Obj(self):
        obj = MessageCommandHandler()

        for i in range(5):
            obj.handle('messages start yeah' + str(i))
        return obj

    def test_get(self):
        obj = self.Obj()
        self.assertEqual('yeah4', obj.handle('messages get'))

    def test_random(self):
        obj = self.Obj()
        print('asd')
        self.assertEqual('yeah3', obj.handle('messages random', rand_func=lambda x, b: 3))


if __name__ == '__main__':
    unittest.main()
