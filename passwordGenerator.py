import random
from tkinter import messagebox
from tkinter import *

passString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def generatePassword():
    try:
        lent = int(len_entry.get())
        rep = int(rep_entry.get())
    except:
        messagebox.showerror(message="Please enter the values required inputs")
        return
    
    if rep == 1:
        if lent > len(passString):
            messagebox.showerror(message="Length of password exceeds the number of unique characters available.")
            return
        password = random.sample(passString, lent)
    elif rep == 2:
        password = random.choices(passString,k=lent)
    else:
        messagebox.showerror(message="Chose a valid choice.")
        return
    
    password = ''.join(password)

    password_var = StringVar()
    password_var.set(f"Generated Password: {password}")

    password_label = Label(password_gen, textvariable=password_var, wraplength=350, fg="black")
    password_label.place(x=20, y=200)


password_gen  = Tk()
password_gen.geometry("400x300")
password_gen.title("Password Generator")
#title of the app
title_label = Label(password_gen, text="Password Generator", font=('Ubuntu Mono',12))
title_label.pack()
#Read length
length_label = Label(password_gen, text="Enter length of password: ")
length_label.place(x=20,y=60)
len_entry = Entry(password_gen, width=3)
len_entry.place(x=320,y=60)
#Read repetition
repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise ")
repeat_label.place(x=20,y=90)
rep_entry = Entry(password_gen, width=3)
rep_entry.place(x=320,y=90)
#Generate password
password_button = Button(password_gen, text="Generate Password", command=generatePassword)
password_button.place(x=100,y=150)
#Exit and close the app
password_gen.mainloop()