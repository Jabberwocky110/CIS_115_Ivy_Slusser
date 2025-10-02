#This code uses a nested loop and prints strings and characters in a list.
def printWordList():
    word = ["Apples", "Bananas", "Pears", "Carrots"]
    for value in word:
        print(value)
        for list in value:
            print(list)
printWordList()