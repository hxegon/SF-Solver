import unittest
from path import Path

class PathTests(unittest.TestCase):

    def setUp(self):
        self.p = Path()
        self.p.goto(1)
        self.p.goto(2)

    def testCanGotoNode(self):
        self.assertEqual(self.p.current, 2)

    def testStoresPath(self):
        self.assertEqual(self.p.history, [1, 2])

    def testStoresLast(self):
        self.assertEqual(self.p.last, 1)

    def testCantGotoNodesTwiceInOnePath(self):
        with self.assertRaises(Exception):
            self.p.goto(1)
