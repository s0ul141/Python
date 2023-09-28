#!/usr/bin/env python
# coding: utf-8

# In[2]:


#wap to count the number of upper case letters and lower case letters
a=input("enter a string :")
u=0
l=0
for i in a:
    if (i>='A' and i<='Z'):
        u+=1
    elif (i>='a' and i<='z'):
        l+=1
print("Number of upper case letters ",+u)
print("Number of lower case letters ",+l)

