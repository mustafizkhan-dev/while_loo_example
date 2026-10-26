# 27. Print all factors of a number
n = int(input("Enter a positive number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
