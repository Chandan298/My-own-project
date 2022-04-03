
from tkinter import *
import random
root = Tk()
root.geometry("300x300")
label = Label(root, font = ("Times New Roman", 40))
def roll():
    dice = ['\u0031','\u0032','\u0033','\u0034','\u0035','\u0036']
    a = random.choice(dice)
    label.config(text = a)
    label.pack()
    
button = Button(root, text="Roll Again", command=roll)
button.pack()
button.place(x = 200, y = 200)
root.mainloop()

# call by value, call by reference.
# roll(), roll.