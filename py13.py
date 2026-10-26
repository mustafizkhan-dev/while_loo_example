# 13. Check whether a number is palindrome
n = int(input("Enter a number: "))
if n >= 0 and str(n) == str(n)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

