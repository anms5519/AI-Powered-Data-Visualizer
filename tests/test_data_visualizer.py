import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import pandas as pd
from src.data_visualizer import DataVisualizer

class TestDataVisualizer(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test
        self.data = pd.DataFrame({
            'column1': [1, 2, 3, 4, 5],
            'column2': [5, 4, 3, 2, 1]
        })
        self.visualizer = DataVisualizer(self.data)

    def test_plot_histogram(self):
        # Test the plot_histogram method
        try:
            self.visualizer.plot_histogram('column1')
        except Exception as e:
            self.fail(f"plot_histogram() raised {type(e).__name__} unexpectedly!")

    def test_plot_scatter(self):
        # Test the plot_scatter method
        try:
            self.visualizer.plot_scatter('column1', 'column2')
        except Exception as e:
            self.fail(f"plot_scatter() raised {type(e).__name__} unexpectedly!")

    def test_plot_heatmap(self):
        # Test the plot_heatmap method
        try:
            self.visualizer.plot_heatmap()
        except Exception as e:
            self.fail(f"plot_heatmap() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
