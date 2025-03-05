num1 = float(input("Enter 1st number :"))
num2 = float(input("Enter 2nd number:"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1*num2

if num2!=0:
    division = num2/num2

else:
    division = "undefined(cannot divide by zero)"

print("\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")