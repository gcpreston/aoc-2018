import unittest

from aoc.day01 import day01


class TestDay01(unittest.TestCase):

    def test_part2(self):
        self.assertEqual(0, day01.part2([1, -1]))
        self.assertEqual(10, day01.part2([3, 3, 4, -2, -4]))
