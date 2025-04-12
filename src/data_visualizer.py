import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_scatter(self, column_x, column_y):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=self.data[column_x], y=self.data[column_y])
        plt.title(f'Scatter Plot of {column_x} vs {column_y}')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.show()

    def plot_heatmap(self):
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Heatmap of Correlation Matrix')
        plt.show()
