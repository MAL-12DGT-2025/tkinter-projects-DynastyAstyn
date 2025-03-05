import tkinter as tk
from tkinter import ttk

root = tk.Tk()
con_var = tk.IntVar()

def convert():
    result_l.config(text = f"{box.get()}")

title = ttk.Label(root, text = "Temperature Converter")
title.grid(column = 0, row = 0, columnspan = 2, padx = 10, pady = 5)

box = ttk.Entry(root)
box.grid(column = 0, row = 1, columnspan = 2, padx = 10, pady = 5)

celcius_to_farenheit = ttk.Radiobutton(root, text = "C to F", variable = con_var, value = 1)
celcius_to_farenheit.grid(column = 0, row = 2, padx = 10)
farenheit_to_celcius = ttk.Radiobutton(root, text = "F to C", variable = con_var, value = 2)
farenheit_to_celcius.grid(column = 1, row = 2, columnspan = 2, padx = 10)

convertingning = ttk.Button(root, text = "Convert", command = convert)
convertingning.grid(column = 0, row = 3, columnspan = 2, padx = 10, pady = 10)

result_l = ttk.Label(root, text = "")
result_l.grid(column = 0, row = 4, columnspan = 2, padx = 10, pady = 10)

root.mainloop()