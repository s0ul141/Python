#!/usr/bin/env python
# coding: utf-8

# matrix addition, substraction and multiplication of nXn matrix element by element

# In[11]:


row=int(input("enter the number of rows :"))
column=int(input("enter the number of columns :"))
l_1=[[int(input("enter for 1st list: ")) for j in range (column)] for i in range (row)]
l_2=[[int(input("enter for 2st list: ")) for j in range (column)] for i in range (row)]
l_sum=[]
l_sub=[]
l_mul=[]
print("1st list ",l_1)
print("2nd list ", l_2)
for i in range (row):
    l_sum.append([])
    l_sub.append([])
    l_mul.append([])
    for j in range (column):
        add=l_1[i][j]+l_2[i][j]
        sub=l_1[i][j]-l_2[i][j]
        mul=l_1[i][j]*l_2[i][j]
        l_sum[i].append(add)
        l_sub[i].append(sub)
        l_mul[i].append(mul)
print("sum of elements ", l_sum)
print("substraction of elements ", l_sub)
print("multiplication of elements ",l_mul)

