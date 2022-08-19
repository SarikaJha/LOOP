# i=1
# num=1
# while i<=4:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         num=num+1
#         j=j+1
#     print( )
#     i=i+1

# i=1
# while i<=4:
#     j=4
#     while j>=i:
#         print(" ",end=" ")
#         j=j-1
#     n=i
#     while n>=1:
#         print("*",end=" ")
#         n=n-1
#     print( )
#     i=i+1

i=1
while i<=4:
    j=4
    while j>=i:
        print(" ",end="")
        j=j-1
    n=i
    while n>=1:
        print("*",end=" ")
        n=n-1
    i=i+1
    print()

    ##SECOND METHOD

n=int(input("enter the number of rows:"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(" ",end="")
        j-=1
    a=i
    while a>=1:
        print("*",end=" ")
        a-=1
    i+=1
    print( )

    ##for loop

num=int(input("enter the number of rows:"))
for i in range(0, num):
     for j in range(0, num-i-1):
          print(end=" ")
     for j in range(0, i+1):
          print("*", end=" ")
     print( )