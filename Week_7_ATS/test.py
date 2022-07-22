import unittest
import randomgame

class TestRandomGame(unittest.TestCase):
    def test_within_range(self):
        test_param = -1
        result = randomgame.within_range(test_param)
        self.assertFalse(result)
    
    def test_is_correct(self):
        test_param = 5
        result = randomgame.is_correct(test_param, test_param)
        self.assertTrue(True)        
        
if __name__ == '__main__':
    unittest.main()