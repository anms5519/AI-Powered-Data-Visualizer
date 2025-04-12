import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from data_visualizer import DataVisualizer

def main():
    # Load data
    data = pd.read_csv('data.csv')

    # Create an instance of DataVisualizer
    visualizer = DataVisualizer(data)

    # Generate visualizations
    visualizer.plot_histogram('column_name')
    visualizer.plot_scatter('column_x', 'column_y')
    visualizer.plot_heatmap()

if __name__ == "__main__":
    main()
