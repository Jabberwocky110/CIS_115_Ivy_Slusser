#This code uses a function to add a value to a string.
def slice_my_string():
    string = input("Enter a string")
    #The string is sliced and assigned to a new variable.
    sliced = string[0:3]
    return sliced
sliced = slice_my_string()
print(sliced)