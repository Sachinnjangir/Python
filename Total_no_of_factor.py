def count_factors(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count

num = 320
num_factors = count_factors(num)
print("The total number of factors of", num, "is:", num_factors)
 