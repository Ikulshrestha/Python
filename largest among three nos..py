# how to take multiple inputs in the same line..
a,b,c =input("Enter three nos").split()
if (a>b) and (a>c):
    print("a is greater")
elif (b>a) and (b>c):
    print("b is greater")
else:
    print("c is greater")
