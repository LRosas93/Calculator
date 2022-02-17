from tkinter import ttk
from tkinter import *

# creates main window (master widget)
root = Tk()
root.title("Calculator")


# function for all buttons to display its value on Entry widget
def add_entry(b):
    nums.set(int(b["text"]))


# mainframe widget acts as container for all widgets inside
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Entry Widget
nums = StringVar()
e = ttk.Entry(mainframe, textvariable=nums).grid(column=0, row=0, columnspan=3, sticky=(N, W, E, S))

# num buttons
button_1 = ttk.Button(mainframe, text="1", command=add_entry).grid(column=0, row=3, sticky=(N, W, E, S))
button_2 = ttk.Button(mainframe, text="2", command=add_entry).grid(column=1, row=3)
button_3 = ttk.Button(mainframe, text="3", command=add_entry).grid(column=2, row=3)
button_4 = ttk.Button(mainframe, text="4", command=add_entry).grid(column=0, row=2, sticky=(N, W, E, S))
button_5 = ttk.Button(mainframe, text="5", command=add_entry).grid(column=1, row=2)
button_6 = ttk.Button(mainframe, text="6", command=add_entry).grid(column=2, row=2)
button_7 = ttk.Button(mainframe, text="7", command=add_entry).grid(column=0, row=1, sticky=(N, W, E, S))
button_8 = ttk.Button(mainframe, text="8", command=add_entry).grid(column=1, row=1)
button_9 = ttk.Button(mainframe, text="9", command=add_entry).grid(column=2, row=1)
button_0 = ttk.Button(mainframe, text="0", command=add_entry).grid(column=1, row=4)


# operations, negatives and decimal point buttons
button_ints = ttk.Button(mainframe, text="+/-").grid(column=0, row=4, sticky=(N, W, E, S))
button_decPoint = ttk.Button(mainframe, text=".").grid(column=2, row=4)
button_divide = ttk.Button(mainframe, text="/").grid(column=3, row=0)
button_mult = ttk.Button(mainframe, text="X").grid(column=3, row=1)
button_add = ttk.Button(mainframe, text="+").grid(column=3, row=2)
button_minus = ttk.Button(mainframe, text="-").grid(column=3, row=3)
button_equal = ttk.Button(mainframe, text="=").grid(column=3, row=4)


# loops through main window
root.mainloop()
