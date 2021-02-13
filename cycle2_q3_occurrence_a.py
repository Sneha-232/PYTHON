#Count the occurrences of ‘a’ within the list.
list_name=['anu','abhimanyu','vinu','reshma','basil']
count=0
for name in list_name:
    for i in name:
        if i=='a':
            count=count+1

print("The List is : ",list_name)
print("The occurrence of 'a': ",count)
