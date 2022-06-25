import unittest
from stamp_duty_calc import *

class TestStampDuty(unittest.TestCase):

    def test_125000_first(self):
        self.assertEqual(0, stamp_duty(125000, True))

    def test_250000_first(self):
        self.assertEqual(0, stamp_duty(250000, True))

    def test_500000_first(self):
        self.assertEqual(10000, stamp_duty(500000, True))

    def test_925000_first(self):
        self.assertEqual(36250, stamp_duty(925000, True))

    def test_1500000_first(self):
        self.assertEqual(93750, stamp_duty(1500000, True))

    def test_2000000_first(self):
        self.assertEqual(153750, stamp_duty(2000000, True))

    def test_125000_second(self):
        self.assertEqual(0, stamp_duty(125000, False))

    def test_250000_second(self):
        self.assertEqual(2500, stamp_duty(250000, False))

    def test_500000_second(self):
        self.assertEqual(15000, stamp_duty(500000, False))

    def test_925000_second(self):
        self.assertEqual(36250, stamp_duty(925000, False))

    def test_1500000_second(self):
        self.assertEqual(93750, stamp_duty(1500000, False))

    def test_2000000_second(self):
        self.assertEqual(153750, stamp_duty(2000000, False))


if __name__ == '__main__':
    unittest.main()