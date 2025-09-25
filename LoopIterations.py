#This code determines how many times a loop iterates, using a loop counter.
def print_iterations():
    val = int(input("How many times do you want the loop to run?"))
    loop_Counter = val + 1
    for val in range(loop_Counter):
        print(loop_Counter)
    print(f'The function call looped {loop_Counter} times.')
print_iterations()