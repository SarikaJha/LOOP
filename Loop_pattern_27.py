n=int(input("enter the number:"))
i=5
while i>=1:
    j=5
    while j>=1:
        if j>i:
            print("*",end=" ")
        else:
            print(chr(j+64),end=" ")
        j=j-1
    i=i-1
    print()