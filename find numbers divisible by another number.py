num=int(input("Enter the number"))
lists=[12,65,45,39,650]
res=list(filter(lambda x: (x % num == 0),lists))
print(res)