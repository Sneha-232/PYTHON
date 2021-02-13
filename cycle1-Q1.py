cr_yr=int(input("Current year :"))
l_yr=int(input("Enter the finsl year :"))
i=cr_yr
print("The Leap Years")
while(i<=l_yr):
    if(i%4==0 or i%400==0 and i%100==0):
        print(i)
    i=i+1;
