#!/usr/bin/env python
# coding: utf-8

# In[21]:


n = int(input("Enter the number of dimensions you want: ")) #give dimensions eg., (x1,y1) 2d (x,y,z)3d ...so on (x,y,z,...n) nd
a = [] #Point A
b = [] #Point B
d=0
for i in range(0, n): #taking input from users
    s = int(input("Enter the values for a: "))
    p = int(input("Enter the values for b: "))
    a.append(s) #appending 
    b.append(p) #appending
print ("coordinates of A are", tuple(a)) #printing as tuple
print ("coordinates of B are", tuple(b)) #printing as tuple
for i in range (0, n): #summation of points 
    d = d+((a[i]-b[i])**2)
d=d**0.5 #sqrt of the summation
print("The Euclidian Distance between the given points are ",+d)

