#This code checks if a credit card is valid.
def validate_credit_card():
    ccNum = input("Enter your credit card number")
    #The number is reversed and assigned to a new variable.
    ccNumReverse = ccNum[::-1]
    cardNumberList = []
    for value in ccNumReverse:
       #Each number in the credit card is placed in a list.
       values = int(value)
       cardNumberList.append(values)
    #The length of the number entered is determined.
    length = len(cardNumberList)
    #Two new lists are created.
    even = []
    odd = []
    count = 0
    #This nested loop enables every other number in the card to be put in a different list.
    while count < length:
     for number in ccNumReverse:
        if count % 2 == 0:
         #The numbers have to be converted to integers again.
         IntNumber = int(number)
         even.append(IntNumber)
         count = count + 1
        else:
          odd.append(number)
          count = count + 1
    #A new list is created when the numbers in one list are multiplied.
    multipliedList = []
    #The numbers in the first list are multiplied by two.
    for num in odd:
        integer = int(num)
        multiplied = (integer * 2)
        multipliedList.append(multiplied)
    NewMultipliedList = []
    #This loop determines if any numbers are greater than nine.
    for Val in multipliedList:
        if Val > 9:
           #For values greater than nine, nine is subtracted from them.
           Val = Val - 9
        NewMultipliedList.append(Val)
    #The two lists are combined to create one list.
    NewcardNumberList = even + NewMultipliedList
    #The values in the combined list are summed. 
    total = sum(NewcardNumberList)
    mod10 = total % 10
    #If the total divied by ten is equal to zero, the code prints valid.
    if mod10 == 0:
       print(f'The credit card number {ccNum} is valid!')
    else:
       print("Invalid credit card number entered. Please try again.")
       #By recalling the function, users can enter another credit card number.
       validate_credit_card()
validate_credit_card()