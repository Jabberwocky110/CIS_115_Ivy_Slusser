#This code determines how many times a loop iterates, using a loop counter.
def print_iterations(val):
    #The loop within the function will determine how many times the loop is run so val is in the function.
    for val in range(val +1):
        print(val)
#Loop_Counter is added here so the user can enter how many times they want the loop to run.
loop_Counter = int(input("How many times do you want the loop to run?"))
print_iterations(loop_Counter)
print(f'The function call looped {loop_Counter} times.')