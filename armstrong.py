num=int(input("value"))
sum=0
ex = len(str(num))
temp = num
while num>0:
    dig =num % 10
    sum+= dig**ex
    num=num//10
if temp==sum:
    print("yes armstrong")
else:
    print("No")