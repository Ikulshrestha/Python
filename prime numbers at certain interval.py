#*to check prime numbers
"""i=int(input(print("enter the number")))
if i>1:
    for x in range(2, i):
        if(i%x==0):
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("prime number")
"""
lower=int(input("Enter the lower number"))
upper=int(input("Enter the upper number"))
print("The numbers between", lower, "and", upper, "are:")

for num in range(lower,upper+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)

