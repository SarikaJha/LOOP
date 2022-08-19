# i=1
# user=int(input("enter the number"))
# while i<=10:
#     print(user,"*",i,"=",user*i)
#     i=i+1

n=int(input("enter the number:"))
i=1
while i<=n:
    j=1
    while j<=10:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    print()