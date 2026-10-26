# 32. Calculate power without using pow()
base = int(input("Enter base: "))
exp = int(input("Enter non-negative exponent: "))
result = 1
for i in range(exp):
    result *= base
print("Answer =", result)
