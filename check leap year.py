i = int(input(print("Enter the year")))
if(i%400==0):
    print("the year is leap year")
elif (i%100==0):
    print("the year is not leap year")
elif(i%4==0):
    print("the year is leap year")
else:
    print("the year is not leap year")