import unittest
from ion_flux_relabeling import *

class Ion_flux_tests(unittest.TestCase):

    def test_height_3(self):

        self.assertEqual([-1,7,6,3], solution(3, [7,3,5,1]))

    def test_height_5(self):

        self.assertEqual([21,15,29], solution(5, [19, 14, 28]))

    def test_height_4(self):

        self.assertEqual([14, 3, -1, 15], solution(4, [13, 2, 15, 7]))

