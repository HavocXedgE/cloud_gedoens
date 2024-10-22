from unittest import TestCase
import unittest


def multiply(a,b):
    return a * b

class Multiplier_Test(TestCase):
    
    def test_multiply(self):
        self.assertEqual(multiply(3,4), 12)
        
        
if __name__ == "__main__":
    unittest.main()