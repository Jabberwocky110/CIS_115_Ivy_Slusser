#This code determines if a number is larger than another number.
num1 = int(input("Enter a number"))
num2 = int(input("Enter a second number"))
numbers = [num1, num2]
Larger_Number = max(numbers)
#The code prints the larger number from the original input.
if num1 is Larger_Number:
    print(f'The larger number is {num1}.')
else:
    print(f'The larger number is {num2}.')