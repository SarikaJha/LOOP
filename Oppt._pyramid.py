n=int(input("enter the number of rows:"))
b=n-1
while b>=1:
    print(" "*(n-b),end=" ")
    k=1
    while k<=b:
        print("*",end=" ")
        k=k+1
    b=b-1
    print( )