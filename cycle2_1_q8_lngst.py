def longest(lst):
    maxl=0
    for i in lst:
        if(len(i)>maxl):
            maxl=len(i)
            temp=i
    print("The word with longest length is ",temp," : length ",maxl)

list1=[]
n=int(input("Enter number of strings :"))
print("Enter strings :")
for i in range(n):
    s=input()
    list1.append(s)
longest(list1)