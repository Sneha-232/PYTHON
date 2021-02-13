#list comparison
list_a=[]
list_b=[]
a=int(input("Enter the number of elemnts in firts list : "))
b=int(input("Enter the number of elemnts in second list : "))

print("Enter the elements of 1st list : ")
for i in range(0,a):
    n=int(input())
    list_a.append(n)


print("Enter the elements of 2nd list : ")
for j in range(0,b):
    n=int(input())
    list_b.append(n)

if len(list_a)==len(list_b):
    print("List are in equal length")
else:
    print("List are not in equal length")

if sum(list_a)==sum(list_b):
    print("List sums are equal")
else:
    print("List sums are not equal")

c=set(list_a).intersection(set(list_b))

if c!=0:
    print("List contains common values")
else:
    print("List not contains common values")