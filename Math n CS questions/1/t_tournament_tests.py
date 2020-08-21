# Contains tests for tennis tournament.

import unittest
from tennis_tournament import *

class TennisTournamentTests(unittest.TestCase):

    def basic_test(self):

        skills = {'Andy' : 7, 'Novak' : 5, 'Roger' : 3,
                  'Rafael' : 2}
        self.AssertEqual('2940764800', solution(skills))
