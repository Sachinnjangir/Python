#method 1 
def sum_factors(x):
    factor_sum = 0
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            factor_sum += i
    return factor_sum

num = 320
factors_sum = sum_factors(num)
print("The sum of factors of", num, "is:", factors_sum)

##Method 2
n=10
sum =0
for i in range(1,n+1):
    if(n%i==0):
        sum = sum+i
print(sum)
