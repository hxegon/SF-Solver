import unittest
from cell import *

class CellTests(unittest.TestCase):
    def testTakesValue(self):
        x = Cell(9)
        self.assertEqual(x.value, 9)
