import tkinter as tk
from tkinter import ttk

def check_password_strength(event=None):
    password = password_entry.get()
    length = len(password)

    if length == 0:
        strength_label.config(text="Enter a password", foreground="gray")
    elif length < 6:
        strength_label.config(text="Weak", foreground="red")
    elif 6 <= length <= 10:
        strength_label.config(text="Medium", foreground="orange")
    else:
        strength_label.config(text="Strong", foreground="green")

# Create the main application window
app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("400x150") # Set a fixed window size

# Create a frame for better organization
main_frame = ttk.Frame(app, padding="10")
main_frame.pack(expand=True, fill="both")

# Label for instruction
instruction_label = ttk.Label(main_frame, text="Enter your password:")
instruction_label.pack(pady=5)

# Entry widget for password input
password_entry = ttk.Entry(main_frame, show="*", width=40)
password_entry.pack(pady=5)
password_entry.focus_set() # Set focus to the entry field when the app starts

# Bind the check_password_strength function to the <KeyRelease> event
# This means the function will be called every time a key is released in the entry field
password_entry.bind("<KeyRelease>", check_password_strength)

# Label to display password strength
strength_label = ttk.Label(main_frame, text="Enter a password", font=("Arial", 12, "bold"), foreground="gray")
strength_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()