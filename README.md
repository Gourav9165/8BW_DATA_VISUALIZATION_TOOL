# 8BW_DATA_VISUALIZATION_TOOL



This code is a simple data visualization tool built using the Tkinter library in Python. It allows users to load data from CSV or Excel files, choose a chart type (Line Chart, Bar Chart, Histogram, or Scatter Plot), and visualize the data. The tool uses pandas for data manipulation and matplotlib for plotting. The main class, DataVisualizationTool, creates a GUI with buttons for loading data and plotting charts. The load_data method uses filedialog to open a file, reads the data using pandas, and enables the plot button. The plot_data method generates a plot based on the selected chart type and displays it in a Tkinter window using matplotlib's FigureCanvasTkAgg. The script includes error handling and provides feedback on data loading success or failure. The supported chart types are Line Chart, Bar Chart, Histogram, and Scatter Plot. The Pie Chart functionality is commented out, but it can be uncommented and implemented if needed. The script runs the tool when executed as the main module.

**1. Importing Libraries:**

The script begins by importing necessary libraries:
tkinter: Provides tools for creating graphical user interfaces (GUIs).
filedialog: A module within tkinter for opening file dialogs.
pandas: Used for data manipulation and analysis.
matplotlib.pyplot: A plotting library for creating visualizations.
FigureCanvasTkAgg: A backend for embedding Matplotlib figures in Tkinter applications.


**2. DataVisualizationTool Class:**

The DataVisualizationTool class encapsulates the functionality of the data visualization tool. Key attributes and methods include:
__init__ method: Initializes the Tkinter window, sets its title and dimensions, and creates buttons and a frame for the chart display.

load_data method: Invoked when the "Load Data" button is pressed. It prompts the user to select a CSV or Excel file using a file dialog. The selected file is loaded into a pandas DataFrame (self.df). If successful, the "Plot Data" button is enabled; otherwise, an error message is printed.

plot_data method: Executes when the "Plot Data" button is pressed. It clears any existing widgets in the Matplotlib frame, creates a Matplotlib figure and axis, and plots the data based on the selected chart type. The resulting chart is displayed in the Tkinter window using FigureCanvasTkAgg.


**3. GUI Elements:**

The script creates a Tkinter window (root) and an instance of the DataVisualizationTool class (app).
The GUI includes buttons for loading data and plotting, a dropdown menu for selecting chart types, and a frame for displaying Matplotlib plots.


**4. Data Loading:**

Users can load data by clicking the "Load Data" button, which opens a file dialog for selecting CSV or Excel files. The selected file is loaded into a pandas DataFrame (self.df), and the "Plot Data" button is enabled.


**5. Data Plotting:**

The "Plot Data" button triggers the creation of Matplotlib plots based on the selected chart type. The script supports Line Chart, Bar Chart, Histogram, and Scatter Plot. Additional functionalities like Pie Chart are commented out but can be implemented.
The Matplotlib figure is embedded in the Tkinter window using FigureCanvasTkAgg, providing an interactive and dynamic visualization experience.


**6. Error Handling:**

The script includes error handling for data loading. If an error occurs during the loading process, an exception is caught, and an error message is printed. This ensures that users receive feedback on the success or failure of the data loading operation.


**7. Main Execution:**

The script checks if it is being run as the main module (if __name__ == "__main__":). If true, it creates the Tkinter root window and runs the data visualization tool within the Tkinter event loop using root.mainloop().


In summary, this script provides a user-friendly data visualization tool that allows users to load data from files and dynamically plot various types of charts. The integration of Tkinter, pandas, and matplotlib makes it accessible for users to explore and visualize data interactively, making it a valuable tool for data analysis and exploration.
