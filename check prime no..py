i= int(input(print("Enter the number")))
if i>1:
    for x in range(2,i):
        if(i%x==0):
            print("not a prime no.")
            break
    else:
            print("prime no.")

else:
    print("not a prime no.")