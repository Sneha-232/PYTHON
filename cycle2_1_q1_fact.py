def fact(n):
    f=1;
    if n < 0:
        print("Factorial not found")
    elif n==0:
       print("factorial=",f)
    else:
        for i in range(1,n+1):
            f=f*i
        print("factorial=",f)

num=int(input("Enter the number :"))
fact(num)