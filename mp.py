import numpy as np
from main import *
from my_code import*

# name = "lala"
# np.savetxt('name.npy', name, delimiter=" ", fmt="%s") 
# d=np.array([])
# np.save('dist.npy',dist)


#pgm to add to dist
# d=getimage()
# dist=np.load("dist.npy").tolist()
# dist.append(d)
# a=np.asarray(dist)
# np.save('dist.npy',a)
#

#pgm to add to name
# name ='lala'
# n=np.load("name.npy").tolist()
# n.append(name)
# a=np.asarray(n)
# np.save('name.npy',a)

#intialize name

name ='lala'
a=np.array([name])
np.save('name.npy',a)


# initialize distance

d= getimage()
a=np.array([d])
np.save('dist.npy',a)



la=1
a=np.array([la])
np.save('label.npy',a)

# n= np.load('name.npy')
# na= np.append(n,['shikha'],axis=0)
# # n=np.load("name.npy").tolist()
# # n.append(name)
# # a=np.asarray(n)
# np.save('name.npy',na)





# dist=np.load("dist.npy")
# arr = [[1,2,3,4,5,6,7]]
# newarr = np.append(dist,arr,axis=0)
# np.save('dist.npy',newarr)


names=np.load("name.npy")
label=np.load("label.npy")
dist=np.load("dist.npy")


for i in names:

	print(i)
for i in dist:
	print(i)
for i in label:
	print(i)



# l = np.load('label.npy').tolist()
# print(l[-1])


# naming=np.load("database/naming.npy")
# print(naming)
# database=np.load("database/data.npy")
# print(database)
# labels=np.load("database/labels.npy")

# for i in naming:
# 	print(i)
# for i in database:
# 	print(i)
# for i in labels:
# 	print(i)





# import numpy as geek 
  
# a = geek.arange(5) 
  
# # a is printed. 
# print("a is:") 
# print(a) 
  
# # the array is saved in the file geekfile.npy  
# geek.save('geekfile', a) 
  
# print("the array is saved in the file geekfile.npy") 