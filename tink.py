import tkinter as tk

root = tk.Tk()

root.title("Tkinter Test")

root.geometry("600x500")

label = tk.Label(root, text="Hello, Tkinter on Windows!")

label.pack(pady=20)

root.mainloop()