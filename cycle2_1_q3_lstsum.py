lst=[]
n=int(input("Enter the number of elements :"))
print("Enter the elements :")
for i in range(n):
    a=int(input())
    lst.append(a)
s=0
for i in lst:
    s=s+i
print('Sum of elements =',s)