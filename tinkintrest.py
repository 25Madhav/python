from tkinter import *
import math

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        # Simple Interest Calculation
        simple_interest = (principal * time * rate) / 100
        simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")

        # Compound Interest Calculation
        # A = P(1 + R/100)^T
        amount = principal * (pow((1 + rate / 100), time))
        compound_interest = amount - principal
        compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        simple_interest_label.config(text="Please enter valid numbers for all fields.")
        compound_interest_label.config(text="")
    except Exception as e:
        simple_interest_label.config(text=f"An error occurred: {e}")
        compound_interest_label.config(text="")

# Create the main window
app = Tk()
app.title("Interest Calculator")
app.geometry("400x300")

# Labels and Entry fields for Principal, Time, Rate
principal_label = Label(app, text="Principal Amount:")
principal_label.pack(pady=5)
principal_entry = Entry(app)
principal_entry.pack()

time_label = Label(app, text="Time Period (Years):")
time_label.pack(pady=5)
time_entry = Entry(app)
time_entry.pack()

rate_label = Label(app, text="Rate of Interest (%):")
rate_label.pack(pady=5)
rate_entry = Entry(app)
rate_entry.pack()

# Calculate Button
calculate_button = Button(app, text="Calculate Interest", command=calculate_interest)
calculate_button.pack(pady=15)

# Result Labels
simple_interest_label = Label(app, text="")
simple_interest_label.pack()

compound_interest_label = Label(app, text="")
compound_interest_label.pack()

# Run the application
app.mainloop()