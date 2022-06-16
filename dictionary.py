# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:07:23 2022

@author: pulle
"""

from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)
label_of_dog = Label(root)

dictionary = {'Mutable': 'Values can be changed just like a list',
              'Immutablem': 'Values can not be changed just like a tuple',
              'Tkinter': 'It is the GUI library of python',
              'Dog': 'a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice'}

def mutable():
    label_of_mutable["text"] = dictionary['Mutable']
    
def immutable():
    label_of_immutable["text"] = dictionary['Immutable']

def tkinter():
    label_of_tkinter["text"] = dictionary['Tkinter']
    
def dog():
    label_of_dog["text"] = dictionary['Dog']
button_mutable = Button(root , text = "Meaning of Mutable",command = mutable)
button_mutable.place(relx = 0.5, rely = 0.2, anchor = CENTER)

label_of_mutable.place(relx = 0.5, rely = 0.3, anchor = CENTER)

button_immutable = Button(root , text = "Meaning of Immutable",command = immutable)
button_immutable.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_of_immutable.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button_tkinter = Button(root , text = "Meaning of Tkinter",command = tkinter)
button_tkinter.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label_of_tkinter.place(relx = 0.5, rely = 0.7, anchor = CENTER)

button_dog = Button(root , text = "Meaning of Dog",command = dog)
button_dog.place(relx = 0.5, rely = 0.8, anchor = CENTER)

label_of_dog.place(relx = 0.5, rely = 0.9, anchor = CENTER)


root.mainloop()