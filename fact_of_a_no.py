# using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=5
result=fact(5)
print(result)

#using math package
from math import factorial
x=5
fact1=factorial(x)
print(fact1)

#using for loop
num =5
factorial=1
if num==0 or num==1:
    print("factorial:",factorial)
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
    
# using for loop
num =1
factorial=1

if num>1:
    for i in range(1,num+1):
        factorial=factorial*i
#elif num==0 or num==1:
else:    
    print("factorial:",factorial)
print(factorial)
