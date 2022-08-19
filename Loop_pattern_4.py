i=1
while i<=5:
     j=1
     while j<=i:
          print(j, end=" ")
          j=j+1
     i=i+1     
     print( )

    ##FOR LOOP

n=int(input("enter the number:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print( )