num=int(input("enter the number"))
length=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**length
    temp//=10
if num==sum:
    print(num,("is an armstrong number"))
else:
    print(num,"is not an armstrong number")             
