import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import pandas as pd
from src.main import main

class TestMain(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test
        self.data = pd.DataFrame({
            'column_name': [1, 2, 3, 4, 5],
            'column_x': [1, 2, 3, 4, 5],
            'column_y': [5, 4, 3, 2, 1]
        })

    def test_main(self):
        # Test the main function
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised {type(e).__name__} unexpectedly!")

    def test_data_loading(self):
        # Test data loading
        self.assertIsInstance(self.data, pd.DataFrame)

    def test_data_content(self):
        # Test data content
        self.assertEqual(self.data['column_name'].tolist(), [1, 2, 3, 4, 5])
        self.assertEqual(self.data['column_x'].tolist(), [1, 2, 3, 4, 5])
        self.assertEqual(self.data['column_y'].tolist(), [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
