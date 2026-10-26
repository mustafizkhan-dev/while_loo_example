# 37. Print numbers until user enters a negative number
while True:
    n = int(input("Enter a number: "))
    if n < 0:
        break
    print(n)
