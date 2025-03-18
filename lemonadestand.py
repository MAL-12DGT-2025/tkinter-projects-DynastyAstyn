import tkinter as tk 
from tkinter import ttk 



root = tk.Tk() 
con_var = tk.IntVar()
root.title('lemony') 
constal = {

    "Lemonade, $1":"1",
    "Strawberry Lemonade $1":"1",
    "Fizzy, $2":"2",
    "Cookie, $2":"2",     

}
cartv = ""
carv = ""
def press(ops):
    global carv
    global cartv
    menop = menu.get()
    if ops == "add":
        cartv =  f"{menop} + {cartv} "
        carv =  str(eval(cartv))
        cart.config(text = f"{cartv} = {carv}")


ttk.Label(root, text = "Lemonade\nStand :p").grid(row = 0, column = 1) 
ttk.Label(root, text = "Select an item :").grid(row = 1, column = 0) 
cart = ttk.Label(root, text = "Cart: ")
cart.grid(row = 6, column = 0)

menu = ttk.Combobox(root, width = 20)
menu.grid(row = 2 , column = 0)

extra = ttk.Combobox(root, width = 25)
extra.grid_remove()

extra['values'] = (

    "Extra sugar +50c",                         
    "Extra lemon +20c",            

)

menu['values'] = (
    
    "Lemonade, $1",
    "Strawberry Lemonade $1",
    "Fizzy, $2",
    "Cookie, $2",     

) 

##normal buttons
button_add = ttk.Button(root, text = "Add to order", command = lambda : press("add"))
button_add.grid(row = 2, column = 2, padx = 5)

button_remove = ttk.Button(root, text = "Remove", command = lambda : press("remove"))
button_remove.grid(row = 3 , column = 2, padx = 5 )

button_pay = ttk.Button(root, text =  "Pay", command = lambda : press("pay"))
button_pay.grid(row = 4 , column = 2, padx = 5)

##radiobuttons
button_small = ttk.Radiobutton(root, text = "Small",  variable = con_var, value = 1)
button_small.grid(row = 2, column = 1, padx = 5)

button_medium = ttk.Radiobutton(root, text = "Medium",  variable = con_var, value = 2)
button_medium.grid(row = 3 , column = 1, padx = 5 )

button_large = ttk.Radiobutton(root, text =  "Large",  variable = con_var, value = 3)
button_large.grid(row = 4 , column = 1, padx = 5)

ice = ttk.Checkbutton(root, text =  "ice")
ice.grid(row = 5 , column = 1)

root.mainloop() 