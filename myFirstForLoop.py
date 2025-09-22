#This code allows the user to determine how many times they want to run a loop
done = False
#Allow the user to enter the amount of iterations
Loop_Iterations = int(input("Enter how many times you want to run the loop"))
#Begin the loop
for num in range(Loop_Iterations):
    print(num)
print("The loop is finished.")