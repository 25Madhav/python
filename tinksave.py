from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile

window = Tk()
window.title("text editor")
window.geometry("600x500")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

txt_edit = Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath.name, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath.name}")

button_frame = Frame(window, relief="raised", bd=2)
button_frame.grid(row=0, column=0, sticky="ns")

btn_open = Button(button_frame, text="Open", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save = Button(button_frame, text="Save As...", command=save_file)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

window.mainloop()