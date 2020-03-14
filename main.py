import os
import sys
import numpy as np
import cv2
import easygui
from my_code import *
def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))
path=easygui.fileopenbox("open the image you want to check on")
img=cv2.imread(path,1)
output,distances,tips,valleys=midfinger(img)
cv2.imshow('FUCK YEAH',output)
cv2.waitKey(0)
print(distances)
d=[]
naming=np.load("database/naming.npy")
database=np.load("database/data.npy")
locations=np.load("database/locations.npy")
labels=np.load("database/labels.npy")
for i in database:
        d.append(dist(distances,i))
temp=np.copy(labels)
d,temp=zip(*sorted(zip(d,temp)))
temp=np.copy(labels)
d,temp=zip(*sorted(zip(d,temp)))
temp=temp[:10]
label=np.bincount(temp).argmax()
for i in temp:
	print (naming[i]," ",)
# print (d)

