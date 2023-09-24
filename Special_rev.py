#!/usr/bin/env python
# coding: utf-8

# In[1]:


a= input("enter an alpha numeric string: ")
res=[] #to store the result 
num='' #to store the digit
for i in a:
    if i.isdigit():
        num = num+ i #joining the digit
    else:
        if num:
            rev= num[::-1] #reversing the digits
            res.append(rev) #appending the digit
            num='' #re-initializing 
        res.append(i) #appending the characters
if num: #adding the last left out digits
    rev = num[::-1]
    res.append(rev) #appending the digit

final = ''.join(res) #type casting it from list to string
print("Here is the out put ",final)

