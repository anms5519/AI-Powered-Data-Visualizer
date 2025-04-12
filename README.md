# AI-Powered Data Visualizer

## Project Description

The AI-Powered Data Visualizer is a tool designed to help users create insightful and visually appealing data visualizations using artificial intelligence. The main features of this project include:
- Automatic data analysis and visualization suggestions
- Support for various types of visualizations (e.g., bar charts, line charts, scatter plots)
- Customizable visualization options
- Easy-to-use command-line interface

## Installation Instructions

### Dependencies

To run the AI-Powered Data Visualizer, you need to have the following dependencies installed:
- Python 3.6 or higher
- Required Python packages (listed in `requirements.txt`)

### Setup Steps

1. Clone the repository:
   ```
   git clone https://github.com/anms5519/AI-Powered-Data-Visualizer.git
   ```
2. Navigate to the project directory:
   ```
   cd AI-Powered-Data-Visualizer
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage Instructions

To use the AI-Powered Data Visualizer, follow these steps:

1. Prepare your data file (e.g., CSV format).
2. Run the main application with the following command:
   ```
   python src/main.py --data <path_to_your_data_file>
   ```
3. The application will analyze your data and provide visualization suggestions.
4. Choose the desired visualization type and customize the options as needed.

### Examples

Here are some examples of how to use the AI-Powered Data Visualizer:

- To visualize a CSV file:
  ```
  python src/main.py --data data/sample.csv
  ```

- To specify a particular type of visualization (e.g., bar chart):
  ```
  python src/main.py --data data/sample.csv --type bar
  ```

### Command-Line Options

- `--data`: Path to the data file (required)
- `--type`: Type of visualization (optional, default: automatic suggestion)
- `--output`: Path to save the generated visualization (optional)
