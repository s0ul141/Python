#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""Exercise 1. Write a Python function named ConvertToArray(str) which takes a string of numbers separated by commas and colon. 
The function should then convert this string into a array of numbers and return
it to the user. For converting the string into array use the following rules:
(i) The colon distinguishes the elements by row i.e., all the values before the colon should be placed in single
row of the array.
(ii) The comma distinguishes the elements by column i.e., all the values separated by comma will be placed in
columns in the same row of the array."""

#defination of the function which is converting a string in to Array
def cta(input_str):
    mat=[]
    row= input_str.split(";")
    
    for i in row:
        if '.' in i:
            col= [float(c) for c in i.split(',')]
        else:
            col= [int(c) for c in i.split(',')]
        mat.append(col)
    print ("Array of Numbers :")
    for i in mat:
        print ("[",*i,"]")  
        
        
#calling the above made function :))
a1= "2,4,5;5,7,1;5,8,3"
a2= "2.4,6.0,5.9;9.8,7.7,9.0;4.3,5.0,2.0"
cta(a1)
cta(a2)

