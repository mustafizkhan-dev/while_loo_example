# 49. Display menu-driven program using while loop
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        break

    if choice not in (1, 2, 3):
        print("Invalid choice")
        continue

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Sum =", a + b)
    elif choice == 2:
        print("Difference =", a - b)
    elif choice == 3:
        print("Product =", a * b)

