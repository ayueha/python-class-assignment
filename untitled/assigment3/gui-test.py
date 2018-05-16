


"""
import tkinter
root = tkinter.Tk()
l = tkinter.Label(root, text="Hello World")
l.pack()
root.mainloop()
"""

import tkinter
def hello():
    print("Hello World")

root = tkinter.Tk()
l = tkinter.Label(root, text="My Button")
l.pack()
b = tkinter.Button(root, text="Push", command=hello)
b.pack()
root.mainloop()

