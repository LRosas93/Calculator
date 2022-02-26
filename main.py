from tkinter import ttk
from tkinter import *

# creates main window (master widget)
root = Tk()
root.title("Calculator")


# keylog for buttons
log = ""
# holds expression to later be evaluated
ep = ""

def keylog(k):
    """log variable just holds button value as its being pressed, to prevent
       bug"""
    operators = "*/+-"
    global log
    for o in operators:
        if o in log:
            log = ""
    log += k
    num.set(log)


# function for 'clear' button
def clear_entry():
    """sets widget value to 0: linked variable: 0"""
    global log
    log = ""
    num.set(0)


def add_op(o):
    """o is an operator to use for calculation"""
    global log, ep
    log += o
    ep = log
    num.set(0)

# performs calculations: status of function: beta function, no implementation
def get_result():
    """ep holds expression to evaluate"""
    global log, ep
    ep += log
    result = eval(ep)
    num.set(result)


# converts ep with num value to its negative
def get_neg():
    global log
    ep = -(int(log))
    num.set(ep)

# mainframe widget acts as container for all widgets inside
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# when window is resized, tk will configure all columns and rows to fill in gaps
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Entry Widget that displays value of button pressed on calculator
num = StringVar()
e = ttk.Entry(mainframe, textvariable=num)
e.grid(column=0, row=0, columnspan=2, sticky=(N, W, E, S))


# num buttons
button_1 = ttk.Button(mainframe, text="1", command=lambda : keylog("1")).grid(column=0, row=3, sticky=(N, W, E, S))
button_2 = ttk.Button(mainframe, text="2", command=lambda : keylog("2")).grid(column=1, row=3)
button_3 = ttk.Button(mainframe, text="3", command=lambda : keylog("3")).grid(column=2, row=3)
button_4 = ttk.Button(mainframe, text="4", command=lambda : keylog("4")).grid(column=0, row=2, sticky=(N, W, E, S))
button_5 = ttk.Button(mainframe, text="5", command=lambda : keylog("5")).grid(column=1, row=2)
button_6 = ttk.Button(mainframe, text="6", command=lambda : keylog("6")).grid(column=2, row=2)
button_7 = ttk.Button(mainframe, text="7", command=lambda : keylog("7")).grid(column=0, row=1, sticky=(N, W, E, S))
button_8 = ttk.Button(mainframe, text="8", command=lambda : keylog("8")).grid(column=1, row=1)
button_9 = ttk.Button(mainframe, text="9", command=lambda : keylog("9")).grid(column=2, row=1)
button_0 = ttk.Button(mainframe, text="0", command=lambda : keylog("0")).grid(column=1, row=4)


# operations, negatives and decimal point buttons
button_ints = ttk.Button(mainframe, text="+/-",  command=get_neg).grid(column=0, row=4, sticky=(N, W, E, S))
button_decPoint = ttk.Button(mainframe, text=".", command=lambda : keylog(".")).grid(column=2, row=4)
button_divide = ttk.Button(mainframe, text="/", command=lambda : add_op("/")).grid(column=3, row=0)
button_mult = ttk.Button(mainframe, text="X", command=lambda : add_op("*")).grid(column=3, row=1)
button_add = ttk.Button(mainframe, text="+", command=lambda : add_op("+")).grid(column=3, row=2)
button_minus = ttk.Button(mainframe, text="-", command=lambda : add_op("-")).grid(column=3, row=3)
button_equal = ttk.Button(mainframe, text="=", command=get_result).grid(column=3, row=4)
button_clear = ttk.Button(mainframe, text="C", command=clear_entry).grid(column=2, row=0)


# adds padding to all child widgets inside mainframe of 5
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


root.mainloop()
