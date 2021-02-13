def string_add(str1,str2):
    new1=str2[0]+str1[1:]
    new2=str1[0]+str2[1:]
    return new1+" "+new2

string1=input("Enter the string1 :")
string2=input("Enter the string2 :")
print(string_add(string1,string2))