# n=int(input("enter the number:"))
# i=1
# while i<=1:
#     if n%2==0 and n!=2:
#         print(n,"is not a prime number")
#     else:
#         print(n,"is a prime number")
#     i=i+1


user=int(input("enter a number:"))
i=1
count=0
while i<=user:
    if user%i==0:
        count+=1
    i+=1
if count==2:
    print(user,"is a prime number!")
else:
    print(user,"is not a prime number!")