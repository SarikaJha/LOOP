string="python"
length=len(string)
i=1
while i<=length:
    j=0
    while j<i:
        print(string[j],end=" ")
        j=j+1
    i=i+1
    print( )

    ##For loops##

str=input("enter the string:")
length=len(str)
for row in range(length):
     for col in range(row+1):
          print(str[col],end=" ")
     print( )