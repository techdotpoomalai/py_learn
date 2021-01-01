# Example 1-28. PP4E\Preview\tkinter103.py

from tkinter import *
from tkinter.messagebox import showinfo
# from plistlib import Image, Image1

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')
top.iconbitmap('D:/PYTHON/py_learn/The_Begnning/tkinter_module/test.ico')   #icons allow .ico extens only 
Label(top, text="Enter your name:").pack(side=TOP)
# img_=Image.PhotoImage(Image1.open('D:/PYTHON/icons/train.jfif'))
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text="Submit", command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)
top.mainloop()