# n=int(input("enter any number of rows:"))
# for i in range(n-1):
#      for j in range(i,n):
#           print(" ", end=" ")
#      for j in range(i+1):
#           print("*", end=" ")
#      for j in range(i):
#           print("*", end=" ")
#      print()
# for i in range(n):
#      for j in range(i+1):
#           print(" ",end=" ")
#      for j in range(i, n-1):
#           print("*", end=" ")
#      for j in range(i,n):
#           print("*", end=" ")
#      print()


n=int(input("enter the rows"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(" ",end='')
        j-=1
    a=i
    while a>=1:
        print("*",end=" ")
        a-=1
    i+=1
    print()
b=n-1
while b>=1:
    print(" "*(n-b),end=" ")
    k=1
    while k<=b:
        print("*",end=" ")
        k=k+1
    b-=1
    print()