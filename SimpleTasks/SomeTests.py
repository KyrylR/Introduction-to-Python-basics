import unittest
from SimpleTasksPython import arrayNesting


class TestDiffTasks(unittest.TestCase):
    def testCase1_arrayNesting(self):
        self.assertEqual(arrayNesting([0, 1, 2]), 1)

    def testCase2_arrayNesting(self):
        self.assertEqual(arrayNesting([0, 2, 1]), 2)

    def testCase3_arrayNesting(self):
        self.assertEqual(arrayNesting([5, 4, 0, 3, 1, 6, 2]), 4)

    def testCase4_arrayNesting(self):
        self.assertEqual(arrayNesting([1, 2, 0, 4, 5, 3]), 3)


if __name__ == '__main__':
    unittest.main()
