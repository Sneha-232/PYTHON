print("Enter 3 number :")
n1=int(input())
n2=int(input())
n3=int(input())
if (n1 > n2) and (n1 > n3):
    print("Largest number : ",n1)
elif(n2 > n1) and (n2 > n3):
    print("Largest number : ",n2)
else:
    print("Largest number : ",n3)
