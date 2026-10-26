# 48. Check whether a number is strong number
n = int(input("Enter a number: "))
total = 0
for ch in str(n):
    if ch.isdigit():
        fact = 1
        for i in range(1, int(ch) + 1):
            fact *= i
        total += fact
if n >= 0 and total == n:
    print("Strong number")
else:
    print("Not a strong number")

