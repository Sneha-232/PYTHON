# Python program to print squares of Numbers in a List 
  
# list
list1 = [] 
n=int(input("Enter number of elements :"))
i=0
while(i<n):
 elem=int(input("enter elemet:"))
 list1.insert(i, elem)
 i=i+1

print("Squares of numbers:")
# iterating each number in list 
for num in list1: 
    
    # print squares  
       print(num*num, end = " ") 