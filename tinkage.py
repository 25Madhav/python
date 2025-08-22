from tkinter import *
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid numbers for Day, Month, and Year.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

app = Tk()
app.title("Age Calculator")
app.geometry("300x200")

day_label = Label(app, text="Day:")
day_label.pack()
day_entry = Entry(app)
day_entry.pack()

month_label = Label(app, text="Month:")
month_label.pack()
month_entry = Entry(app)
month_entry.pack()

year_label = Label(app, text="Year:")
year_label.pack()
year_entry = Entry(app)
year_entry.pack()

calculate_button = Button(app, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

result_label = Label(app, text="")
result_label.pack()

app.mainloop()