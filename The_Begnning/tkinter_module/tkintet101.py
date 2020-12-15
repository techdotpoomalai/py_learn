# Example 1-24. PP4E\Preview\ tkinter101.py

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed...!')

window = Tk()
button = Button(window, text='press the button', command=reply)

button.pack()
window.mainloop()