import tkinter as tk
from tkinter import ttk

root = tk.Tk()

title = ttk.Label(root, text = "Temperature\nConverter").grid(row = 0)
box = ttk.Entry(root).grid(row = 1)
celcius_to_farenheit = ttk.Radiobutton(root, text = "C to F").grid(column = 0, row = 2)
farenheit_to_celcius = ttk.Radiobutton(root, text = "F to C").grid(column = 1, row = 2)
convert = ttk.Button(root, text = "Convert").grid(column = 0, row = 3)


root.mainloop()