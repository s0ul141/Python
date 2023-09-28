#!/usr/bin/env python
# coding: utf-8

# In[1]:


#wap to count the number of digits, alphabets and special characters
a=input("enter a string :")
d=0
c=0
s=0
for i in a:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        c+=1
    else:
        s+=1
print("Number of digits are ",+d)
print("Number of alphabets are ",+c)
print("Number of special characters are ",+s)

