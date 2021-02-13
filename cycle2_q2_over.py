#all values greater than 100, store ‘over’ instead.
list1=[]
n=int(input("Enter the number of elements : "))

for i in range(0,n):
    elmnt=int(input("Eenter Number : "))
    if elmnt>100:
        #append 'over' if element>100
        list1.append("Over")
    else:
        list1.append(elmnt)

print(list1)