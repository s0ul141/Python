'''Ratul made a linked list, a list made of n nodes, where every node has two variables, the velocity and the mass of a particle.
Since all the particles have the velocity in the same direction, find the total momentum of the entity made by the particles from the linked list.'''


x= int(input('number of attributes N '))
c=0
for i in range(x):
  m,v=map(int,input("enter mass m and velocity v ").split())
  c+= m*v
print(c)


'''n = int(input("Value: "))
l = []
for i in range(n):
    s = list(map(int,input().split()))
    l.append(s)
    s=0
total = 0
for i in range(n):
    total = total+ (l[i][0]*l[i][1]) 

print(total)'''