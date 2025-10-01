num1 = input("Enter a first number")
num2 = input("Enter a second number")
difference = int(num1) - int(num2)
print(f'The difference is {difference}')
if difference < 0:
    print("Invalid! The value is less than zero.")
else:
    print("The values entered were valid integers.")