#LCM of two numbers using GCD function
def computegcd(x,y):
    while y:
        x,y=y,x%y
    return x
def lcm(x,y):
    i=(x*y) // computegcd(x,y)
    return i
num1=int(input("Enter the first number"))
num2=int(input("Enter the secomd number"))
print("The LCM of",num1,"and",num2,"is: ",lcm(num1,num2))