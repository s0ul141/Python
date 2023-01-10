'''multiplication of two matrix
variables ->
d - for storing the dimensions of the matrix which we will multiply
a - empty list, for matrix 1
b - empty list, for matrix 2
c - empty list, for product matrix
functions ->
split() - function is used to separate the input given by user, by using ',' '''

d=int(input(print"enter dimensions"))
a=[]
b=[]
c=[]
for i in range(d): #loop to take input 
    e=[int(i) for i in input().split(",")] #temp variable 'e' for taking input 
    a.append([i for i in e]) #here the values of e is appended in the list a
for i in range(d): #loop to take input
    f=[int(i) for i in input().split(",")] #temp variable 'f' for taking input
    b.append([i for i in f]) #here the values of f is appended in the list b
for i in range(d):
   c.append([]) #row initialization
   for j in range(d):
       c[i].append(0) #column initialization along with, zero is being appended in every column
for i in range(d): #row loop
    for j in range(d): #column loop
        for k in range(d): #product loop
            c[i][j]=c[i][j]+a[i][k]*b[k][j] #here multiplication is happening between a and b
l=""
for i in range(d): #loop for out put matrix C
    for j in c[i]:
        l=l+str(j)+","
    print(l[:-1])
    l=""