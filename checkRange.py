#This code enables the user to input a number in the range of 0 to 100
Minimum = 0
Maximum = 100
Number = int(input("Enter a number"))
done = False
#The loop continues until a number out of range is entered
while Number < Maximum and Number > Minimum:
    Number = int(input("Enter a new number"))
if Number > Maximum:
    print("Sorry the number you entered is out of range!")
if Number < Minimum:
    print("Sorry the number you entered is out of range!")
    
    