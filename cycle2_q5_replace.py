#replace character
str=input("Enter a String :")
word=list(str)
ch=word[0]
length=len(word)
for i in range(1,length):
    if word[i]==ch:
        word[i]='$'
print(word)
