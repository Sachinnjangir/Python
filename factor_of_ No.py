## Method 1
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 15
print_factors(num)

## Method 2

n=15
for i in range(1,n+1):
    if n%i==0:
        print(i)
        
## Method 3

n = 15
factors = [i for i in range(1, n + 1) if n % i == 0]
print("Factors of",n,"is:",factors)
