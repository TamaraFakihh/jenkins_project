import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from app import greet

class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Tamara Fakih!")

if __name__ == "__main__":
    unittest.main()
