import unittest
import main


class TestMain(unittest.TestCase):
    def test_simple_func_checkDirectWork_True(self):
        test_param = 10
        result = main.simple_func(test_param)
        self.assertEqual(result, 15)

    def test_simple_func_checkStringParam_True(self):
        test_param = 'aas'
        result = main.simple_func(test_param)
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
