# Example 1-25. PP4E\Preview\tkinter102.py

from tkinter import *
from tkinter.messagebox import showinfo


class test():
    def __init__(self):
        pass
    def reply(self):
        showinfo(title='Message Tab Heading', message='top level this is Message Tob message')

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        # button = Button(self, text='press', command=test().reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='Button pressed!')



if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()