# Example 1-26. PP4E\Preview\attachgui.py

from tkinter import *
from tkinter102 import MyGui

# main app window
mainwin = Tk()
Label(mainwin, text='Main Tab').pack()

# popup window
popup = Toplevel()
# popup=Tk()
Label(popup, text='Attach Tab').pack(side=LEFT)
MyGui(popup).pack(side=TOP) # attach my frame side allow only top,buttom,right ,left
mainwin.mainloop()
# popup.mainloop()