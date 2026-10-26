# 47. Find product of digits of a number
n = abs(int(input("Enter a number: ")))
product = 1
if n == 0:
    product = 0
while n > 0:
    product *= n % 10
    n //= 10
print("Product of digits =", product)