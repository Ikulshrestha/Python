terms=int(input("Enter the number"))
for num in range(terms):
    n=lambda x : x ** num
    print(n(2))