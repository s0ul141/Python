#!/usr/bin/env python
# coding: utf-8

# In[21]:


"""Exercise 3. Write a function ArrayOperations(array1,array2,operation) where the operation
is either add, subtract and dotproduct. Then the function should perform the operations of addition,
subtraction and element-wise multiplication respectively on the arrays array1 and array2.
Remark: Please note that, for the specified operations to be performed both arrays should have same dimension
and to check this, you can use the above function ArraySize."""

size=ArraySize #something ArraySize is there and there is the code 

def ArrayOperations(a1, a2, op):
    
    d_a1=size(a1)
    d_a2=size(a2)
    #checking Dimensions of the array
    if d_a1 == d_a2 :
        r=len(a1)
        for i in a1:
            c=len(i)
            
        #Addition    
        if op == "add":
            add=[]
            for i in range(r):
                add.append([])
                for j in range(c):
                    add[i].append(a1[i][j]+a2[i][j])
            print ("Addition is:")
            for i in add:
                print ("[", *i, "]")

        #Subtract
        elif op == "sub":
            sub=[]
            for i in a1:
                c=len(i)
            for i in range(r):
                sub.append([])
                for j in range(c):
                    sub[i].append(a1[i][j]-a2[i][j])
            print ("Subtraction is:")
            for i in sub:
                print ("[", *i, "]")
                
        #Dotproduct
        elif op == "dot":
            #creating the result matrix
            result=[]
            for i in range(len(a1)):
                result.append([])
                for j in range(len(a1[i])):
                    result[i].append(0)
            for i in range(len(a1)):
                for j in range(len(a2[0])):
                    for k in range(len(a2)):
                        result[i][j] += a1[i][k] * a2[k][j]
            
            print("Dotproduct is:")
            for i in result:
                print(i) 
        else:
            print("Input array with proper dimension UwU")
            
#calling
a1=[[1,2,8],[2,4,3],[4,7,1]]
a2=[[5,6,9],[4,7,1],[3,5,1]]

op="add"
ArrayOperations(a1, a2, op)
op="dot"
ArrayOperations(a1, a2, op)
op="sub"
ArrayOperations(a1, a2, op)

