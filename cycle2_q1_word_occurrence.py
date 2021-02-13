#Count the occurrences of each word in a line of text.
def occurence(str):
    words=str.split()
    counts=dict()
    for wrd in words:
        if wrd in counts:
            #increment the count of words
            counts[wrd]=counts[wrd]+1
        else:
            counts[wrd]=1
    return counts

string=input("Enter the string : ")
print(occurence(string))
        