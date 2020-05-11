from tkinter import*
from tkinter import messagebox
from main import *
from my_code import*
import numpy as np
import cv2

def clickone ():
	adduser()

def clicktwo():
	name=checker()
	messagebox.showinfo("Result","User is "+name)



root =Tk()
root.minsize(300, 400) 
root.title("Hand Geometry Verification System")
label = Label(root, text="WELCOME TO HAND GEOMETRY VERIFICATION SYSTEM",font =('Verdana', 20))
bt1 = Button(root, text= "Add new user",command=clickone)
bt2 = Button(root, text= "Verify user",command=clicktwo)


label.grid(row =0,column=0, columnspan=2, padx=10,pady=10)
bt1.grid(row =1,column=0,padx=50,pady=20)
bt2.grid(row =1,column=1,padx=50,pady=20)
root.mainloop()