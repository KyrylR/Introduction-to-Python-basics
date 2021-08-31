import unittest
import Python_Moduls


class TestRandomGame(unittest.TestCase):
    def test_correctInput(self):
        result = Python_Moduls.run_guess(5, 5)
        self.assertTrue(result)

    def test_wrongInput(self):
        result = Python_Moduls.run_guess(6, 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
