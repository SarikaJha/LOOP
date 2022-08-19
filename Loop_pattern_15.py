i=1
while i<=5:
    j=1
    while j<=i:
        if i%2==0:
            print(chr(64+i),end=" ")
        else:
            print(i,end=" ")
        j=j+1
    print( )
    i=i+1