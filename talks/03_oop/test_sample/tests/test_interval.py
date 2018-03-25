import unittest
from unittest.mock import patch
from datetime import datetime

from interval import TimeInterval

class TimeIntervalTestCase(unittest.TestCase):
    def test_str(self):
        interval = TimeInterval(
            datetime(2017, 1, 1),
            datetime(2018, 1, 1),
        )
        
        self.assertEqual(
            str(interval),
            '2017-01-01 00:00:00 -> 2018-01-01 00:00:00'
        )

# test_init
# patch
# setUp
