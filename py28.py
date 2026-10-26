# 28. Check whether a number is Armstrong
n = int(input("Enter a number: "))
digits = str(n)
total = 0
if n >= 0:
    for ch in digits:
        total += int(ch) ** len(digits)
if n >= 0 and total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
