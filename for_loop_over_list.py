#This function counts the iterations in a loop, using a list.
def getMyList():
    Numbers_By_Ten = [10, 20, 30, 40, 50, 60]
    #The counter is started.
    iterations = 0
    for num in Numbers_By_Ten:
        print(num)
        iterations = iterations + 1
    print(f'The number of iterations is {iterations}.')
getMyList()
    