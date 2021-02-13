dict={}
str=input("Enter the string :")
for i in str:
    key_s=dict.keys()
    if i in key_s:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print("Character freqency : ",dict)