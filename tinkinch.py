import tkinter as tk
from tkinter import ttk

def convert_length():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} centimeters")
    except ValueError:
        result_label.config(text="Please enter a valid number for inches.")

# Create the main window
app = tk.Tk()
app.title("Inches to Centimeters Converter")

# Create a frame for better organization
frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input field for inches
label_inches = ttk.Label(frame, text="Length in Inches:")
label_inches.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_inches = ttk.Entry(frame, width=20)
entry_inches.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Convert button
convert_button = ttk.Button(frame, text="Convert", command=convert_length)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(frame, text="Result will appear here.")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

# Run the application
app.mainloop()