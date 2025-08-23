from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
messagebox.showwarning("window name","text to be displayed")
def msg():
    messagebox.showwarning("ALERT STOP VIRUS FOUND!")
button=Button(root,text="scan for virus",command=msg)
button.place(x=40,y=80)
root.mainloop()