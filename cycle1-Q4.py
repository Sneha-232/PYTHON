# Python program to vowels in string 
  
# Code #1 
string=input("Enter the string : ")
i=0
list1=[]

# Iterate over the string 
for elem in string: 
    if(elem=='a'or elem=='e'or elem=='i'or elem=='o'or elem=='u'):
        list1.insert(i,elem)
        i=i+1

print("Vowels in the string :")
for elem in list1: 
     print(elem, end=' ') 

  
  