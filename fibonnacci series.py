n1=0
n2=1
count=0
num=int(input("Upto how many terms "))
if num<=0:
    print("Enter valid terms")
elif num==1:
    print("Fibonnacci series upto",num,":")
    print(n1)
else:
    print("Fibonnacci series upto", num, ":")
    while count<num:
        print(n1,end=',')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

