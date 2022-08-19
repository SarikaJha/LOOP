#A string is said to be palindrome if the reverse of the string is the same as string. 

n=int(input("enter number"))
temp=n
rev=0
while(n>0):
     digit=n%10
     rev=rev*10+digit
     n=n//10
if(temp==rev):
     print("the number is a palindrome!")
else:
     print("the number isn't o palindrime!")