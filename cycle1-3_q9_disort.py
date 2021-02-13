d={'manu':58,'yadhu':65,'basil':70,'anu':59}
print("The dictionary is",d)

d1=list(d.items())
d1.sort()

print("The dictionary in ascending order is",d1)

d1.sort(reverse=True)

print("The dictionary in descending order is",d1)
