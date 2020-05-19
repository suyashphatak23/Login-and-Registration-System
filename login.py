'''
Registration and Login System : Login Module
@author : Suyash Shivaji Phatak
Date: 12/5/2020
'''

# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3 

# Creating Input

def Log():
    # Creating a new window
    Login = tk.Tk()
    Login.geometry('500x500')
    Login.title('Login to System !')

    # Background Colors
    Login.configure(background='#3B2C35')

    # Locking the window size
    Login.resizable(width=False, height=False)

    # Creating title icon
    Login.iconbitmap('img/loginlogo.ico')

    # Top Frame
    top_frame = Label(Login, text='Login To System',font = ('Cosmic', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Login, padx=40, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Creating function for connecting to database and checking username
    def Search(arg = None):
        if username_entry.get() == '': 
            ms.showerror('Oops', 'Enter Username !!')
            
        elif password_entry.get() == '':
            ms.showerror('Oops', 'Enter Password !!')
            
        else:
            global username
            username = username_entry.get()
            global password
            password = password_entry.get()

            # Making connection
            conn = sqlite3.connect('Database.db')

            # Creating cursor
            with conn:
                cursor = conn.cursor()

            # Searching for users
            find_user = ('SELECT * FROM users WHERE Username = ? AND Password = ?')
            cursor.execute(find_user,(username, password))
            results = cursor.fetchall()

            # if user then new window
            if results:
                Login.destroy()
                result = tk.Tk()
                result.geometry('500x500')
                result.title('Thank You !')

                # Background Colors
                result.configure()

                # Locking the window size
                result.resizable(width=False, height=False)

                # Showing Result
                label = tk.Label(result, text = 'Hi '+ username +'\nThank You For Using Our System !!!!',font=('Arial',12, 'bold'),bg='white', fg='green').place(relx = 0.5, rely = 0.5, anchor = CENTER)

            # if user do not exist
            else:
                ms.showerror('Oops','User Not Found !! Check Username and Password Again !!')

    # creating a label for username and password using Label 
    username = tk.Label(frame, text = 'Username',font=('Arial',12, 'bold'),bg='white', fg='green')
    password = tk.Label(frame, text = 'Password', font = ('Arial',12,'bold'),bg='white', fg='green')   

    # creating a entry for username 
    username_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='#FBB13C')
    username_entry.bind('<Return>', Search)
    password_entry=tk.Entry(frame, font = ('calibre',10,'normal'), show = '*', justify = 'center', bg='#FBB13C') 
    password_entry.bind('<Return>', Search)
    
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Login', command = Search, width="10",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5') 

    # Placing the label and entry   
    username.pack()
    username_entry.focus_set()
    username_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit = tk.Button(Login, text = "Quit", width="10", command = Login.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)
