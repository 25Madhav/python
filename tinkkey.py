from tkinter import *
window=Tk()
window.title("event handler")
window.geometry("100x100")
def handle_keypress(event):
    print(event.char)
    window.bind("<key>",handle_keypress)
def handle_click(event):
    print("The button was click")
button=Button(text="click me!")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()