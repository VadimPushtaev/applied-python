# -*- encoding: utf-8 -*-

from unittest import TestCase

# from grep import grep, parse_args
import grep

lst = []


def save_to_list(line):
    lst.append(line)


grep.output = save_to_list


class GrepBaseTest(TestCase):

    lines = ['baab', 'bbb', 'ccc']

    def tearDown(self):
        global lst
        lst.clear()

    def test_base_scenario(self):
        params = grep.parse_args(['aa'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab'])

    def test_base_scenario_multi(self):
        params = grep.parse_args(['b'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'bbb'])

    def test_base_scenario_count(self):
        params = grep.parse_args(['-c', 'a'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1'])

    def test_base_scenario_invert(self):
        params = grep.parse_args(['-v', 'b'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['ccc'])
