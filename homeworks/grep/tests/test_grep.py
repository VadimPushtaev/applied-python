
from unittest import TestCase

import grep

lst = []


def save_to_list(line):
    lst.append(line)


grep.output = save_to_list

class GrepBaseTest(TestCase):

    lines = ['baab', 'bbb', 'ccc', 'A']

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
        self.assertEqual(lst, ['ccc', 'A'])

    def test_base_scenario_case(self):
        params = grep.parse_args(['-i', 'a'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'A'])

class GrepPatternTest(TestCase):

    lines = ['baab', 'abbb', 'fc', 'AA']

    def tearDown(self):
        global lst
        lst.clear()

    def test_question_base(self):
        params = grep.parse_args(['?b'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb'])

    def test_question_start(self):
        params = grep.parse_args(['?a'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab'])

    def test_queston_end(self):
        params = grep.parse_args(['c?'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, [])

    def test_queston_double(self):
        params = grep.parse_args(['b??b'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab'])

    def test_queston_count(self):
        params = grep.parse_args(['???'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb'])

    def test_asterics(self):
        params = grep.parse_args(['b*b'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb'])

    def test_asterics_all(self):
        params = grep.parse_args(['***'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, self.lines)

class GrepContextTest(TestCase):

    lines = ['vr','baab', 'abbb', 'fc', 'bbb', 'cc']

    def tearDown(self):
        global lst
        lst.clear()

    def test_context_base(self):
        params = grep.parse_args(['-C1','aa'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['vr', 'baab', 'abbb'])

    def test_context_intersection(self):
        params = grep.parse_args(['-C1','ab'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['vr', 'baab', 'abbb', 'fc'])

    def test_context_intersection_hard(self):
        params = grep.parse_args(['-C2','bbb'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, self.lines)

    def test_before(self):
        params = grep.parse_args(['-B1','bbb'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb', 'fc', 'bbb'])

    def test_after(self):
        params = grep.parse_args(['-A1','bbb'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['abbb', 'fc', 'bbb', 'cc'])

class GrepLineNumbersTest(TestCase):

    lines = ['vr','baab', 'abbb', 'fc', 'bbb', 'cc']

    def tearDown(self):
        global lst
        lst.clear()

    def test_numbers_base(self):
        params = grep.parse_args(['-n','ab'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2:baab', '3:abbb'])

    def test_numbers_context(self):
        params = grep.parse_args(['-n', '-C1','aa'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3-abbb'])

    def test_numbers_context_question(self):
        params = grep.parse_args(['-n', '-C1', '???'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3:abbb', '4-fc', '5:bbb', '6-cc'])
