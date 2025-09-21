#This program determines the amount of grades a user has entered.
done = False
count = 0

#Ask the user how many grades they will enter
grades_number = int(input("How many grades will you enter?"))
#This prevents the amount of grades from being over 10.
while (grades_number > 10):
   print("Error, please enter another number")
   grades_number = int(input("Enter a different number of grades"))
#Begin Loop
while count < grades_number:
   count = count + 1
   grade = int(input("Enter a grade"))
   print(f'The grade entered is {grade}')
   if(count >= grades_number): 
      print(f'You inputed {grades_number} grades')
