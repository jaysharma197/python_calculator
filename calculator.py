num1 = float(input("Please enter the first number: "))
operator = input("Please Enter a valid operator: ")
num2 = float(input("Please enter the second number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("There was an error, try changing the operator")
