def computehcf(x,y):
    while y:
        x,y=y,x%y
    return x
computehcf(300,400)
print("The HCF is",computehcf(300,400))
#HCF using EUCLIDIAN'S THEOREM
