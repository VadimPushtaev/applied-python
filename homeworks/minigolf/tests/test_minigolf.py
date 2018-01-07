from unittest import TestCase

from minigolf import HitsMatch, Player

class HitsMatchTestCase(TestCase):
    def test_scenario(self):
        m = HitsMatch(3, [Player('A'), Player('B'), Player('C')])

        self._first_hole(m)
        self._second_hole(m)
        self._third_hole(m)

    def _first_hole(self, m):
        m.hit()     # 1
        m.hit()     # 2
        m.hit(True) # 3
        m.hit(True) # 1
        for _ in range(9):
            m.hit() # 2

        self.assertFalse(m.finished)
        self.assertEqual(m.get_table(), [
            (2, 10, 1),
            (None, None, None),
            (None, None, None),
        ])

    def _second_hole(self, m):
        m.hit() # 2
        for _ in range(3):
            m.hit(True) # 3, 1, 2

        self.assertFalse(m.finished)
        self.assertEqual(m.get_table(), [
            (2, 10, 1),
            (1, 2, 1),
            (None, None, None),
        ])

    def _third_hole(self, m):
        m.hit()     # 3
        m.hit(True) # 1
        m.hit()     # 2
        self.assertEqual(m.get_table(), [
            (2, 10, 1),
            (1, 2, 1),
            (1, None, None),
        ])
        m.hit(True) # 3
        m.hit()     # 2
        m.hit(True) # 2

        self.assertTrue(m.finished)
        self.assertEqual(m.get_table(), [
            (2, 10, 1),
            (1, 2, 1),
            (1, 3, 2),
        ])

