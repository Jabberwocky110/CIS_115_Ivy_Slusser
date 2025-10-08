Initial_Value = input("Enter a value")
def append_to_list():
    list = [Initial_Value]
    Next_Value = input("Enter another value")
    list.append(Next_Value)
    Keep_Going = True
    while Keep_Going:
        answer = input("Would you like to enter another value to append to the list? (y or n).")
        if answer == "y":
            Loop_Value = input("Enter your new value")
            list.append(Loop_Value)
        else:
            print(list)
            Keep_Going = False
append_to_list()
