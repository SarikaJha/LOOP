from operator import ilshift


i=1
while i<=5:
    j=5
    while j>i:
        print(" ",end=" ")
        j=j-1

    a=1
    while a<=j:
        print(a,end=" ")
        a=a+1
    print( )
    i=i+1