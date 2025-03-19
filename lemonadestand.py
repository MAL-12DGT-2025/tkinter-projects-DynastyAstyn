import tkinter as tk 
from tkinter import ttk 



root = tk.Tk() 
con_var = tk.IntVar()
root.title('lemony') 

##dictionary for the menu
thing = {

    "Lemonade, +$1":"1",
    "Strawberry Lemonade, +$1.50":"1.5",
    "Fizzy, +$2":"2",
    "Cookie, +$2":"2" ,
    "Brownie, +$2.50" : "2.5"   

}

##dictionary for extras
other_thing = {

    "Extra sugar +50¢" : "0.5",
    "Extra lemon +20¢" : "0.2"

}
thingys_in_the_thing = []
price = float()

def press(thingels):
    global price
    if thingels == "add":
        thingys_in_the_thing.append(menu.get())
        thingys_in_the_thing.append(extra.get())
        price += float(thing[menu.get()]) 
        price += float(other_thing[extra.get()])

        if con_var.get() == 1:
            thingys_in_the_thing.append("Small")
            price -= 0.2
        elif con_var.get() == 2:
            thingys_in_the_thing.append("Large")
            price += 0.5
        price = round(price, 2)

        print(price)
        print(thingys_in_the_thing)

        size = "Large" if con_var.get() == 2 else "Small" if con_var.get() == 1 else ""
        item = menu.get().split(" +")[0]
        extra_item = extra.get().split(" +")[0]
        
        cart_text = f"Cart: {size} {item} with {extra_item}\nTotal: ${price:.2f}" if size else f"Cart: {item} with {extra_item}\nTotal: ${price:.2f}"
        cart.config(text=cart_text)


ttk.Label(root, text = "Lemonade\nStand :p").grid(row = 0, column = 1) 
ttk.Label(root, text = "Select an item :").grid(row = 1, column = 0) 
cart = ttk.Label(root, text = "Cart: ")
cart.grid(row = 6, column = 0)

menu = ttk.Combobox(root, width = 25)
menu.grid(row = 2 , column = 0)

extra = ttk.Combobox(root, width = 25)
extra.grid(row = 3, column = 0)

extra['values'] = (

    "Extra sugar +50¢",                         
    "Extra lemon +20¢",            

)

menu['values'] = (
    
    "Lemonade, +$1",
    "Strawberry Lemonade, +$1.50",
    "Fizzy, +$2",
    "Cookie, +$2",
    "Brownie, +$2.50"    

) 

##normal buttons
button_add = ttk.Button(root, text = "Add to order", command = lambda : press("add"))
button_add.grid(row = 2, column = 2, padx = 5)

button_remove = ttk.Button(root, text = "Remove", command = lambda : press("remove"))
button_remove.grid(row = 3 , column = 2, padx = 5 )

button_pay = ttk.Button(root, text =  "Pay", command = lambda : press("pay"))
button_pay.grid(row = 4 , column = 2, padx = 5)

##radiobuttons
button_small = ttk.Radiobutton(root, text = "Small, -20¢",  variable = con_var, value = 1)
button_small.grid(row = 2, column = 1, padx = 5)

button_large = ttk.Radiobutton(root, text =  "Large +50¢",  variable = con_var, value = 2)
button_large.grid(row = 3 , column = 1, padx = 5)

ice = ttk.Checkbutton(root, text =  "Ice +50¢")  ##ice checkbox
ice.grid(row = 5 , column = 1)

root.mainloop() 