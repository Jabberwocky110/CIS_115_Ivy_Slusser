#This program implements a dictionary of student grades and calculates the average grade of the class.
def calculate_average_grade():
    student_grades = {

    }
    keep_going = True
    #While True the loop for grades continues.
    while keep_going is True:
       name = input("What is the student's name?")
       grade = input("What is their grade?")
       student_grades[name] = int(grade)
       #The loop continues until the user doesn't want to input anymore grades.
       answer = input("Do you want to enter more grades? (yes or no)")
       #The loop repeats based on user input.
       if answer == "yes":
           keep_going is True
       else:
           #The dictionary of student names and grades is printed.
           print(f"Here are the students'names and their grades: {student_grades}")
           #The values from the dictionary are returned and assigned to a variable.
           values = student_grades.values()
           #The sum for all of the students' grades is caluclated.
           sum_for_all_students = sum(values)
           amount_of_dictionary_values = len(student_grades)
           #The average grade for the class is calculated, using the sum of the grades and length of the dictionary.
           average_for_all_students = sum_for_all_students/amount_of_dictionary_values
           print(f'The average grade for all of the students in the class is {average_for_all_students}')
           #The loop is ended.
           keep_going = False
calculate_average_grade()