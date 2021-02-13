# Python program to print positive Numbers in a List 
  
# list
list1 = [] 
n=int(input("Enter number of elements :"))
i=0
while(i<n):
 elem=int(input("enter elemet:"))
 list1.insert(i, elem)
 i=i+1
  
# iterating each number in list 
for num in list1: 
    
    # checking condition 
    if num >= 0: 
       print(num, end = " ") 