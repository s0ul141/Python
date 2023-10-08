#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Exercise 2. Write a function named ArraySize(array) which accepts a list of numbers and returns its
dimension (i.e., number of rows and columns). For example, if the array = [1,2,3,4] then the output
should be (1,4). If the array = [[1,2,3,4],[5,6,7,8]] then the output should be (2,4).

Hint: You can use the len() function to obtain the number of elements."""


#function giving the dimensions 

def ArraySize(array):
    flag = False
    col=0
    row=0
    for item in array:
        if isinstance(item, list):
            flag = True
            break 
    if flag: 
        row=len(d2)
        for i in d2:
            col=len(i)
        dim=(row, col)
        return dim
    else:
        row=1
        col=len(d1)
        dim=(row, col)
        return dim


#calling the function
d1= [1,2,3,4]
d2=[[1,2,3,4], [5,6,7,8]]
d_d1=ArraySize(d1) 
d_d2=ArraySize(d2)
print("the dimension is :", d_d1)
print("the dimension is :", d_d2)

