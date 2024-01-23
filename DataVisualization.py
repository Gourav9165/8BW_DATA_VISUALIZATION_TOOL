import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualization Tool")
        self.root.geometry("900x600")

        self.df = None

        self.load_button = tk.Button(root, text="Load Data", command=self.load_data)
        self.load_button.pack(pady=10)

        self.chart_type_var = tk.StringVar()
        self.chart_type_var.set("Select Chart")

        self.chart_type_menu = tk.OptionMenu(root, self.chart_type_var, "Line Chart", "Bar Chart", "Histogram", "Scatter Plot")
        self.chart_type_menu.pack(pady=10)

        self.plot_button = tk.Button(root, text="Plot Data", command=self.plot_data, state=tk.DISABLED)
        self.plot_button.pack(pady=10)

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(padx=10, pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])

        if file_path:
            try:
                if file_path.endswith(".csv"):
                    self.df = pd.read_csv(file_path)
                elif file_path.endswith(".xlsx"):
                    self.df = pd.read_excel(file_path)
                self.plot_button.config(state=tk.NORMAL)
                print("Data loaded successfully.")
            except Exception as e:
                print(f"Error loading data: {e}")
                self.df = None

    def plot_data(self):
        if self.df is not None:
            for widget in self.canvas_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(figsize=(9, 6))

            chart_type = self.chart_type_var.get()
            if chart_type == "Line Chart":
                self.df.plot(ax=ax)
            elif chart_type == "Bar Chart":
                self.df.plot.bar(ax=ax)
            elif chart_type == "Scatter Plot":
                if "Units" in self.df.columns and "Total" in self.df.columns:  # Check if the columns exist
                    self.df.plot.scatter(x="Units", y="Total", ax=ax)
                else:
                    print("Required columns 'X-axis' and 'Y-axis' not found.")
            elif chart_type == "Histogram":
                self.df.plot.hist(ax=ax)

            ax.set_title("Data Visualization")
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")

            canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        else:
            print("No data to plot.")

root = tk.Tk()
app = DataVisualizationTool(root)
root.mainloop()
