import unittest
from command_handler.message import MessageCommandHandler
from unittest.mock import patch
from random import randint


class MyTestCase(unittest.TestCase):

    # def setUp(self):
    #     self.obj = MessageCommandHandler()
    #     for i in range(5):
    #         self.obj.handle('_start yeah' + str(i))
    def Obj(self):
        obj = MessageCommandHandler()

        for i in range(5):
            obj.handle('_start yeah' + str(i))
        return obj

    def test_get(self):
        obj = self.Obj()
        self.assertEqual('yeah4', obj.handle('_get'))

    def test_random(self):
        obj = self.Obj()
        self.assertEqual('yeah3', obj.handle('_random', rand_func=lambda x, b: 3))







if __name__ == '__main__':
    unittest.main()
