import tkinter as tk
from tkinter import ttk
import random

things = ["rock, paper, scissors"]

def choice(thing):
    comp_choice = random.randrange(0,3)
    if thing != things[comp_choice]:
        if thing == things[0] and comp_choice == things[2] or thing == things[1] and comp_choice == things[0] or thing == things[2] and comp_choice == things[1]:
            thingels.congfig(root)

root = tk.Tk()
root.title("rockokcokco")

rps = ttk.Label(root, text = f'Rcok, paptr\nscissor game')
rps.grid(column = 1, row = 0)

instructions = ttk.Label(root, text = 'make your choice')
instructions.grid (column = 1, row = 1)

thingels = ttk.Label(root, text = '')
thingels.grid (column = 1, row = 2)

rcok = ttk.Button(root, text = 'rcok', command = lambda : choice("rock"))
rcok.grid(column = 0, row = 3)

paper = ttk.Button(root, text = 'paper', command = lambda : choice("paper"))
paper.grid(column = 1, row = 3)

scissor = ttk.Button(root, text = 'scissors', command = lambda : choice("scissors"))
scissor.grid(column = 2, row = 3)

root.mainloop()