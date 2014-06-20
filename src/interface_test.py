import unittest
import interface

class InterfaceTests(unittest.TestCase):

    # No simple test that works for scores_for, but confidence is high that it works

    def testNewPuzzle(self):
        # not a %100 guarantee of correctness
        for i in interface.new_puzzle():
            self.assertTrue(i in range(1, 10))

    def testNormalizesNumStrings(self):
        test = interface.normalize_nums('1234123412341234')
        self.assertEqual(test, [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])

        test = interface.normalize_nums([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
        self.assertEqual(test, [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
