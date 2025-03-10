import tkinter as tk
from tkinter import ttk
import random

things = ["rock", "paper", "scissors"]
scoring = 0

def choice(thing):
    global scoring
    comp_choice = random.randrange(0,3)
    if thing != things[comp_choice]:
        if (thing == things[0] and comp_choice == 2) or (thing == things[1] and comp_choice == 0) or (thing == things[2] and comp_choice == 1):
            thingels.config(text = f"You won, computer picked {things[comp_choice]}")
            scoring += 1
            score.config(text = f"Score : {str(scoring)}")
        else:
            thingels.config(text = f"You lost, computer picked {things[comp_choice]}")
    else:
        thingels.config(text = f"Draw! Select again")

root = tk.Tk()
root.title("rockokcokco")   

rps = ttk.Label(root, text = f'Rcok, paptr, scissor game')
rps.grid(column = 1, row = 0)

thingels = ttk.Label(root, text = 'make your choice')
thingels.grid (column = 1, row = 1)

score = ttk.Label(root, text = 'Score : 0')
score.grid (column = 1, row = 2)

rcok = ttk.Button(root, text = 'rcok', command = lambda : choice("rock"))
rcok.grid(column = 0, row = 3)

paper = ttk.Button(root, text = 'paper', command = lambda : choice("paper"))
paper.grid(column = 1, row = 3)

scissor = ttk.Button(root, text = 'scissors', command = lambda : choice("scissors"))
scissor.grid(column = 2, row = 3)

root.mainloop()