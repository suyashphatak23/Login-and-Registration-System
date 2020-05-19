'''
Registration and Login System
@author : Suyash Shivaji Phatak
Date: 12/5/2020
'''

# Importing tkinter and login, register libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from login import Log
from register import Register
from PIL import ImageTk, Image

''' Window Setting Start '''
# Creating Widget
system = tk.Tk()

# Creating size of window
system.geometry('500x500')

# Background Colors
system.configure(background='#3B2C35')

# Locking the window size
system.resizable(width=False, height=False)

# Creating Title
system.title('Login and Registration System')

# Creating title icon
system.iconbitmap('img/Logo.ico')
''' Window Setting End '''

# Top Frame
top_frame = Label(system, text='WELCOME TO THE SYSTEM',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
top_frame.pack(side='top')


''' Background Image Start'''
# Sizing Image
canvas = Canvas(system, width=500, height=350)

# Opening Image
image = ImageTk.PhotoImage(Image.open('img/car.jpg'))

#Positioning Image
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()
''' Background Image End'''

# Creating Frame
frame = LabelFrame(system,text='SERVICES', padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


# Creating login button and positioning it
login = tk.Button(frame, text = "Login", width="10", bd = '3', command = Log, font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='5')
login.pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()

# Creating and Positioning Button in Main Frame    
register = tk.Button(frame, text = "Register", width="10", bd = '3',  command = Register, font = ('Times', 12, 'bold'), bg='#2A1F2D',fg='white', relief='groove', justify = 'center', pady='5')
register.pack()

# Quit Button of main frame 

def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
    if response == 1:
        system.destroy()
    else:
        pass
    
Quit = tk.Button(system, text = "Quit", width="10", command = Quit, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
Quit.place(anchor ='sw',rely=1,relx=0.775)

# Displyaing Widget to Screen
system.mainloop()
    
