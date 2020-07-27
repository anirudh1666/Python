# Contains tests for google foobar chal 2.2

import unittest
from dont_get_volunteered import *

class DontGetVolunteered(unittest.TestCase):

    def test_calc_neighbours(self):
        self.assertEqual([60, 62, 28, 30, 55, 39, 51, 35], calc_neighbours(45))

    def test_calc_neighbours_second(self):
        self.assertEqual([38, 6, 29, 13], calc_neighbours(23))

    def base_case(self):
        self.assertEqual(3, solution(0, 1))
        

    def test_1(self):
        self.assertEqual(1, solution(19, 36))
        

    def test_2(self):
        pass
        
