import unittest
from score import Score

class ScoreTest(unittest.TestCase):

    def setUp(self):
        self.score = Score(0)

    def testAddingWorks(self):
        self.score.add_from([5, 5, 4])
        self.assertEqual(self.score.total, 29)
        self.score.add(3)
        self.assertEqual(self.score.total, 87)

    def testKeepsTrackOfScoreString(self):
        self.score.add_from([1, 2, 3, 4, 5])
        self.assertEqual(self.score.string, [0, 1, 2, 3, 4, 5])
