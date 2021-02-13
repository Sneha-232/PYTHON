n=int(input("Enter the number of steps :"))
for i in range(n+1):
    c=i
    for j in range(i):
        print(c,end=" ")
        c=c+i
    print()