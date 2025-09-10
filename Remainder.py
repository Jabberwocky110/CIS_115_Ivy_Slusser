num1 = input("Enter a number")
num2 = int(2)
remainder = int(num1) % (num2)
print(f'The remainder is {remainder}')
if remainder > 0:
    print("Odd")
else:
    print("Even")