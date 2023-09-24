#!/usr/bin/env python
# coding: utf-8

# In[5]:


#This code accepts a list of integers (-ve or +ve) and sum of squares of +ve int, sum  of cube of -ve int


n=10 #a/c we have to accepts the list of 10 so we are assigning 'n' with 10
l=[] # initializing an empty list
neg_sum=0 #initializing neg_sum to store the sum of -ve int
pos_sum=0 #initializing pos_sum to store the sum of +ve int
for i in range (0, n): 
    s= int(input("Enter an Integer :")) 
    l.append(s) #appending items to the list 'l'
for i in range (0, n):
    if (l[i]>0):
        pos_sum=pos_sum+(l[i]**2)
    else:
        neg_sum=neg_sum+(l[i]**3)
print ("Sum of Square of Positive Integers", +pos_sum)
print ("Sum of Cube of Negative Integers", +neg_sum)

