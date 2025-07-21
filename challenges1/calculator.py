num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
x = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
match x:
    case 1:
        result = num1 + num2
        print()
    case 2:
        result = num1 - num2
    case 3:
        result = num1 * num2
    case 4:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
        print("Error: Division by zero is not allowed.")
    case _:
        result = "Invalid operation selected."
        print("Invalid operation selected.")
print(f"The result is: {result}")

