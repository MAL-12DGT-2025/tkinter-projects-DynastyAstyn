import tkinter as tk
from tkinter import ttk


def press(thingy):
    c_thing = equation.get()
    c_thing = c_thing + thingy
    print(c_thing)
    equation.set(c_thing)

def clear():
    equation.set("")

def calcing():
    try:
        result = eval(calc.get())
        equation.set(result)
    except :
        equation.set("ERROR")

root = tk.Tk()
root.title("Calculator")

equation = tk.StringVar()

calc = ttk.Entry(root, textvariable = equation)
calc.grid(column = 0, row = 0, columnspan = 4, pady = 5, ipadx = 90)

        ## 1st row of buttons
button7 = ttk.Button(root, text = "7", command = lambda : press("7"))
button7.grid(column = 0, row = 1)

button8 = ttk.Button(root, text = "8", command = lambda : press("8"))
button8.grid(column = 1, row = 1)

button9 = ttk.Button(root, text = "9", command = lambda : press("9"))
button9.grid(column = 2, row = 1)

button_divide = ttk.Button(root, text = "÷", command = lambda : press(" / "))
button_divide.grid(column = 3, row = 1)

        ## 2nd row of buttons
button4 = ttk.Button(root, text = "4", command = lambda : press("4"))
button4.grid(column = 0, row = 2)

button5 = ttk.Button(root, text = "5", command = lambda : press("5"))
button5.grid(column = 1, row = 2)

button6 = ttk.Button(root, text = "6", command = lambda : press("6"))
button6.grid(column = 2, row = 2)

button_times = ttk.Button(root, text = "×", command = lambda : press(" * "))
button_times.grid(column = 3, row = 2)

        ## 3rd row of buttons
button1 = ttk.Button(root, text = "1", command = lambda : press("1"))
button1.grid(column = 0, row = 3)

button2 = ttk.Button(root, text = "2", command = lambda : press("2"))
button2.grid(column = 1, row = 3)

button3 = ttk.Button(root, text = "3", command = lambda : press("3"))
button3.grid(column = 2, row = 3)

button_minus = ttk.Button(root, text = "-", command = lambda : press(" - "))
button_minus.grid(column = 3, row = 3)

        ## 4th row of buttons
button_clear = ttk.Button(root, text = "C", command = clear)
button_clear.grid(column = 0, row = 4)

button0 = ttk.Button(root, text = "0", command = lambda : press("0"))
button0.grid(column = 1, row = 4)

button_equal = ttk.Button(root, text = "=", command = calcing)
button_equal.grid(column = 2, row = 4)

button_plus = ttk.Button(root, text = "+", command = lambda : press(" + "))
button_plus.grid(column = 3, row = 4)

root.mainloop()