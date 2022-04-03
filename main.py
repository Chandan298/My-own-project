from tkinter import *
import random
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("Dice rolling sim")
frm = Frame(root, padding=20)
frm.grid
def dice():
       value = [1, 2, 3, 4, 5, 6]
       result = random.choice(value)
       
       if result == 1:
              label = Label(text="You rolled a one" ,font = ("Times New Roman", 60))
       
       elif result == 2:
              label = Label(text = "You rolled a two", font=("Times New Roman", 60))
              
       elif result == 3:
              label = Label(text = "You rolled a three", font=("Times New Roman", 60))
              
       elif result == 4:
              label = Label(text = "You rolled a four", font=("Times New Roman", 60))
              
       elif result == 5:
              label = Label(text = "You rolled a five", font=("Times New Roman", 60))
              
       elif result == 6:
              label = Label(text = "You rolled a six", font=("Times New Roman", 60))
        
button =  Button(root, text="roll again")
dice()                     
root.mainloop()