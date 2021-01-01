# for good time
from tkinter import *
import random

fontsize = 30
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'black']
# colors = ['yellow', 'green']



def onSpam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='This is text color', bg=random.choice(colors), fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)

def onFlip():
    mainLabel.config(fg=random.choice(colors))
    # c=Tk()
    # d=Label(c, Text='eriereuriueireuiru reiur')
    # d.pack()
    main.after(500, onFlip)

def onGrow():
    global fontsize
    fontsize += 5
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(5000, onGrow)

main = Tk()
mainLabel = Label(main, text='Fun Gui!', relief=RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'), fg='yellow',bg='green')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)     #expand is increas diamention and fill is which demention increasesd
Button(main, text='spam', command=onSpam).pack(fill=X)
Button(main, text='flip', command=onFlip).pack(fill=X)
Button(main, text='grow', command=onGrow).pack(fill=X)
main.mainloop()
