i=1
sum=0
while i<=11:
    weight=int(input("enter the weight"))
    sum=sum+weight
    i=i+1
print(sum)
avg=sum/11
print(avg)
if avg%5==0:
    print(avg,"is divisible by 5")
else:
    print(avg,"is not divisible by 5")