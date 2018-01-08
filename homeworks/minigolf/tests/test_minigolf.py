from unittest import TestCase

from minigolf import HitsMatch, HolesMatch, Player

class HitsMatchTestCase(TestCase):
    def test_scenario(self):
        players = [Player('A'), Player('B'), Player('C')]
        m = HitsMatch(3, players)

        self._first_hole(m)
        self._second_hole(m)

        with self.assertRaises(RuntimeError):
            m.get_winners()

        self._third_hole(m)

        with self.assertRaises(RuntimeError):
            m.hit()

        self.assertEqual(m.get_winners(), [
            players[0], players[2]
        ])

    def _first_hole(self, m):
        m.hit()     # 1
        m.hit()     # 2
        m.hit(True) # 3
        m.hit(True) # 1
        for _ in range(8):
            m.hit() # 2

        self.assertFalse(m.finished)
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
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
            ('A', 'B', 'C'),
            (2, 10, 1),
            (1, 2, 1),
            (None, None, None),
        ])

    def _third_hole(self, m):
        m.hit()     # 3
        m.hit(True) # 1
        m.hit()     # 2
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
            (2, 10, 1),
            (1, 2, 1),
            (1, None, None),
        ])
        m.hit(True) # 3
        m.hit()     # 2
        m.hit(True) # 2

        self.assertTrue(m.finished)
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
            (2, 10, 1),
            (1, 2, 1),
            (1, 3, 2),
        ])


class HolesMatchTestCase(TestCase):
    def test_scenario(self):
        players = [Player('A'), Player('B'), Player('C')]
        m = HolesMatch(3, players)

        self._first_hole(m)
        self._second_hole(m)

        with self.assertRaises(RuntimeError):
            m.get_winners()

        self._third_hole(m)

        with self.assertRaises(RuntimeError):
            m.hit()

        self.assertEqual(m.get_winners(), [
            players[0], players[2]
        ])

    def _first_hole(self, m):
        m.hit(True) # 1
        m.hit()     # 2
        m.hit()     # 3

        self.assertFalse(m.finished)
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
            (1, 0, 0),
            (None, None, None),
            (None, None, None),
        ])

    def _second_hole(self, m):
        for _ in range(10):
            for _ in range(3):
                m.hit() # 2, 3, 1

        self.assertFalse(m.finished)
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
            (1, 0, 0),
            (0, 0, 0),
            (None, None, None),
        ])

    def _third_hole(self, m):
        for _ in range(3):
            m.hit() # 3, 1, 2
        m.hit(True) # 3
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
            (1, 0, 0),
            (0, 0, 0),
            (None, None, 1),
        ])
        m.hit()     # 1
        m.hit(True) # 2

        self.assertTrue(m.finished)
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
            (1, 0, 0),
            (0, 0, 0),
            (0, 1, 1),
        ])

