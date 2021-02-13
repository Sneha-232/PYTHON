def fun_ing(str):
    if(len(str)>=2):
        if(str[-3:]=='ing'):
            str=str+"ly"
        else:
            str=str+"ing"
    print("New string is ",str)

s=input("Enter a string :")
fun_ing(s)
