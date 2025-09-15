#This program determines the amount of grades a user has entered.
done = False
count = 0
grades_number = int(input("How many grades will you enter?"))
while count < grades_number:
   count = count + 1
   grade = int(input("Enter a grade"))
   print(f'The grade entered is {grade}')
   if(count >= grades_number): 
      print(f'The user is done entering {grades_number} grades')
