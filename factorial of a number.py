num=int(input("Enter the number"))
f=1
if(num<0):
    print("Factorial does not exist for negative numbers ")
elif(num==0):
    print("Factorial of zero is 1")
else:
    for i in range(1,num+1):
        f=f*i
    print("Factorial of",num,"is:",f)