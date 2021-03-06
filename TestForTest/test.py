import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('About test func!')

    def test_simple_func_checkDirectWork_True(self):
        '''
        Hi!
        :return: Nothing!
        '''
        test_param = 10
        result = main.simple_func(test_param)
        self.assertEqual(result, 15)

    def test_simple_func_checkString_True(self):
        test_param = 'aas'
        result = main.simple_func(test_param)
        self.assertIsInstance(result, ValueError)

    def test_simple_func_checkNone_True(self):
        test_param = None
        result = main.simple_func(test_param)
        self.assertEqual(result, 'Please enter a number!')

    def tearDown(self) -> None:
        print('cleaning up!')


if __name__ == '__main__':
    unittest.main()
