import unittest
from unittest import result 
import main

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print("About to test a function")
        
    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, 15)
        
    def test_do_stuff2(self):
        test_param = 'sdjffr'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
        
    def test_do_stuff3(self):
        test_param = -1
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Value must be greater than 0')
        
    def test_do_stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)  
        self.assertIsInstance(result, TypeError)
        
        
if __name__ == '__main__':
    unittest.main()