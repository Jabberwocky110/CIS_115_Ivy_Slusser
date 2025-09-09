num1 = input("Enter first number")
num2 = input("Enter second number")
num3 = input("Enter third number")
sum = int(num1) + int(num2)
quotient = float(sum)/float(num3)
print(f'The result is {quotient}')
if quotient > 0:
 print("The matematical operation is > 0")
else:
 print("The matematical operation is <= 0")