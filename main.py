import os
import sys
import numpy as np
import cv2
import easygui
from my_code import *
from tkinter import*

def addname(name,num):

	n= np.load('name.npy')
	na= np.append(n,[str(name)],axis=0)
	print(na)
	# n=np.load("name.npy").tolist()
	# n.append(name)
	# a=np.asarray(n)
	np.save('name.npy',na)
	l = np.load('label.npy')#.tolist()
	x=l[-1]
	for i in range(int(num)):
		d=getimage()
		# f=np.array([d])
		dist= np.load('dist.npy')
		# print("dist")
		# print(dist)
		# dist=np.load("dist.npy").tolist()
		# print("newArray")
		newArray= np.append(dist,[d],axis=0)
		# print(newArray)
		# dist.append(d)
		# a=np.asarray(dist)
		np.save('dist.npy',newArray)

		l=np.load('label.npy')
		la=np.append(l,[x+1],axis=0)
		# l.append(x+1)
		# la=np.asarray(l)
		np.save('label.npy',la)

	messagebox.showinfo("Success","User added successfully")



def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))
def getimage():
	path=easygui.fileopenbox("open the image you want to check on")
	img=cv2.imread(path,1)
	output,distances,tips,valleys=midfinger(img)
	# cv2.imshow('FUCK YEAH',output)
	# cv2.waitKey(0)
	return distances

def checker():
	# print(distances)
	distances=getimage()
	d=[]
	naming=np.load("name.npy")
	database=np.load("dist.npy")
	labels=np.load("label.npy")

	# for i in naming:
	# 	print(i)
	# for i in database:
	# 	print(i)
	# for i in locations:
	# 	print(i)
	# for i in labels:
	# 	print(i)

	for i in database:
	    d.append(dist(distances,i))
	temp=np.copy(labels)
	d,temp=zip(*sorted(zip(d,temp)))
	# temp=temp[:10]
	# label=np.bincount(temp).argmax()
	# la=np.argmax(np.bincount(temp))
	la= temp[0]
	print(la)
	# for i in temp:
	# 	print (naming[i]," ",)
	if d>0:
		return("not Found")
	print (naming[la-1]," ",)
	return str(naming[la-1])

def adduser():
	root =Tk()
	root.minsize(300, 400)
	root.title("User Details")
	label = Label(root, text="USER DETAILS",font =('Verdana', 20))
	la1= Label(root,text="Enter name")
	e1= Entry(root)
	b1= Button(root,text ="Enter")
	la2= Label(root,text="How many images")
	e2= Entry(root)
	b2= Button(root,text ="Enter",command= lambda: addname(e1.get(),e2.get()))
	label.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
	la1.grid(row=1,column=0,padx=10,pady=10)
	e1.grid(row=1,column=1,padx=10,pady=10)
	b1.grid(row=1,column=2,padx=10,pady=10)
	la2.grid(row=2,column=0,padx=10,pady=10)
	e2.grid(row=2,column=1,padx=10,pady=10)
	b2.grid(row=2,column=2,padx=10,pady=10)
	root.mainloop()








