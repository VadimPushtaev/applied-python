
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


class GrepBaseMyTests(TestCase):

    lines = ['baab', 'bbb', 'ccc', 'A']

    def tearDown(self):
        global lst
        lst.clear()

    def test_base1(self):
        params = grep.parse_args(['a'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab'])

    def test_base2(self):
        params = grep.parse_args(['a', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['bbb', 'ccc', 'A'])

    def test_base3(self):
        params = grep.parse_args(['a', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'A'])

    def test_base4(self):
        params = grep.parse_args(['a', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['bbb', 'ccc'])

    def test_base5(self):
        params = grep.parse_args(['aa'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab'])

    def test_base6(self):
        params = grep.parse_args(['aa', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['bbb', 'ccc', 'A'])

    def test_base7(self):
        params = grep.parse_args(['aa', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab'])

    def test_base8(self):
        params = grep.parse_args(['aa', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['bbb', 'ccc', 'A'])

    def test_base9(self):
        params = grep.parse_args(['b'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'bbb'])

    def test_base10(self):
        params = grep.parse_args(['b', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['ccc', 'A'])

    def test_base11(self):
        params = grep.parse_args(['b', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'bbb'])

    def test_base12(self):
        params = grep.parse_args(['b', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['ccc', 'A'])

    def test_base13(self):
        params = grep.parse_args(['c'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['ccc'])

    def test_base14(self):
        params = grep.parse_args(['c', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'bbb', 'A'])

    def test_base15(self):
        params = grep.parse_args(['c', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['ccc'])

    def test_base16(self):
        params = grep.parse_args(['c', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'bbb', 'A'])

    def test_base17(self):
        params = grep.parse_args(['c', '-c'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1'])

    def test_base18(self):
        params = grep.parse_args(['c', '-c', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1'])

    def test_base19(self):
        params = grep.parse_args(['c', '-c', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['3'])

    def test_base20(self):
        params = grep.parse_args(['a', '-c'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1'])

    def test_base21(self):
        params = grep.parse_args(['a', '-c', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2'])

    def test_base22(self):
        params = grep.parse_args(['a', '-c', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2'])

    def test_base23(self):
        params = grep.parse_args(['aa', '-c'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1'])

    def test_base24(self):
        params = grep.parse_args(['aa', '-c', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1'])

    def test_base25(self):
        params = grep.parse_args(['aa', '-c', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['3'])

    def test_base26(self):
        params = grep.parse_args(['b', '-c'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2'])

    def test_base27(self):
        params = grep.parse_args(['b', '-c', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2'])

    def test_base28(self):
        params = grep.parse_args(['b', '-c', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2'])

class GrepPatternMyTests(TestCase):

    lines = ['baab', 'abbb', 'fc', 'AA']

    def tearDown(self):
        global lst
        lst.clear()

    def test_pattern1(self):
        params = grep.parse_args(['*a'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb'])

    def test_pattern2(self):
        params = grep.parse_args(['*a', '-i'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb', 'AA'])
    
    def test_pattern3(self):
        params = grep.parse_args(['*a', '-i', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['fc'])

    def test_pattern4(self):
        params = grep.parse_args(['?b', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['fc', 'AA'])

    def test_pattern5(self):
        params = grep.parse_args(['b*?b'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb'])

    def test_pattern6(self):
        params = grep.parse_args(['????'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb'])

    def test_pattern7(self):
        params = grep.parse_args(['????', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['fc', 'AA'])

    def test_pattern8(self):
        params = grep.parse_args(['a*a'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab'])
 
    def test_pattern9(self):
        params = grep.parse_args(['a*a', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['abbb', 'fc', 'AA'])

class GrepContextMyTests(TestCase):

    lines = ['vr','baab', 'abbb', 'fc', 'bbb', 'cc']

    def tearDown(self):
        global lst
        lst.clear()

    def test_context1(self):
        params = grep.parse_args(['aa', '-B1'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['vr', 'baab'])

    def test_context2(self):
        params = grep.parse_args(['aa', '-B1', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab'])

    def test_context3(self):
        params = grep.parse_args(['aa', '-B1', '-n', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1:vr', '2-baab', '3:abbb', '4:fc', '5:bbb', '6:cc'])

    def test_context4(self):
        params = grep.parse_args(['a', '-B2'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['vr', 'baab', 'abbb'])

    def test_context5(self):
        params = grep.parse_args(['a', '-B2', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3:abbb'])

    def test_context6(self):
        params = grep.parse_args(['a', '-B2', '-n', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1:vr', '2-baab', '3-abbb', '4:fc', '5:bbb', '6:cc'])

    def test_context7(self):
        params = grep.parse_args(['aa', '-A1'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb'])

    def test_context8(self):
        params = grep.parse_args(['aa', '-A2'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb', 'fc'])

    def test_context9(self):
        params = grep.parse_args(['aa', '-A1', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2:baab', '3-abbb'])

    def test_context10(self):
        params = grep.parse_args(['aa', '-A2', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2:baab', '3-abbb', '4-fc'])

    def test_context11(self):
        params = grep.parse_args(['aa', '-A1', '-n', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1:vr', '2-baab', '3:abbb', '4:fc', '5:bbb', '6:cc'])

class GrepContextMyTests2(TestCase):

    lines = ['vr', 'baab', 'abbb', 'fc', 'fc', 'fc', 'bbb', 'cc', 'cc', 'cc', 'cc']

    def tearDown(self):
        global lst
        lst.clear()

    def test_context2_1(self):
        params = grep.parse_args(['b', '-A1'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['baab', 'abbb', 'fc', '--', 'bbb', 'cc'])

    def test_context2_2(self):
        params = grep.parse_args(['b', '-A1', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['vr', 'baab', '--', 'fc', 'fc', 'fc', 'bbb', 'cc', 'cc', 'cc', 'cc'])

    def test_context2_3(self):
        params = grep.parse_args(['b', '-A2', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['2:baab', '3:abbb', '4-fc', '5-fc', '--', '7:bbb', '8-cc', '9-cc'])

    def test_context2_4(self):
        params = grep.parse_args(['b', '-B2'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['vr', 'baab', 'abbb', '--', 'fc', 'fc', 'bbb'])

    def test_context2_5(self):
        params = grep.parse_args(['b', '-B2', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3:abbb', '--', '5-fc', '6-fc', '7:bbb'])

    def test_context2_6(self):
        params = grep.parse_args(['b', '-B2', '-n', '-v'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1:vr', '2-baab', '3-abbb', '4:fc', '5:fc', '6:fc', '7-bbb', '8:cc', '9:cc', '10:cc', '11:cc'])

    def test_context2_7(self):
        params = grep.parse_args(['a', '-C2'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['vr', 'baab', 'abbb', 'fc', 'fc'])

    def test_context2_8(self):
        params = grep.parse_args(['ab', '-C3', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3:abbb', '4-fc', '5-fc', '6-fc'])

    def test_context2_9(self):
        params = grep.parse_args(['ba', '-C2', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3-abbb', '4-fc'])

    def test_context2_10(self):
        params = grep.parse_args(['???', '-C1', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3:abbb', '4-fc', '--', '6-fc', '7:bbb', '8-cc'])

    def test_context2_11(self):
        params = grep.parse_args(['v*', '-B2', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1:vr'])

    def test_context2_12(self):
        params = grep.parse_args(['a??', '-C2', '-n'])
        grep.grep(self.lines, params)
        self.assertEqual(lst, ['1-vr', '2:baab', '3:abbb', '4-fc', '5-fc'])
