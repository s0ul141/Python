#!/usr/bin/env python
# coding: utf-8

# In[8]:


n = int(input("Enter the number of stars you want "))
for i in range (n, -1, -1):
    for j in range (0, i):
        print ("*", end="")
    print()
    

