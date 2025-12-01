#This code enables two users to play a game of TicTacToe.
#Create a variable to end the game.
End = False
#This function determines whether the end conditions have been met for the first player.
def EndConditionsX():
 #The ending variable has to be global.
 global End
 #The indexs with X in the array determine whether the game has been ended.
 for index, values in enumerate(TicTacToeArray):
    #This determines if there is an X on every row.
    if values[0] == "X" and values[1] == "X" and values[2] == "X":
      print("Player One wins!")
      #Here, the game is ended.
      End = True
    else:
         #These if statements determine if there is an X on every column with the same index in each list.
         if all(sublist[0] == "X" for sublist in TicTacToeArray):
          print("Player One wins!")
          #The game is ended, and Player One wins is only printed once.
          End = True
          break
         #This determines if the middle column is all X.
         elif all(sublist[1] == "X" for sublist in TicTacToeArray):
          print("Player One wins!")
          End = True
          break
         elif all(sublist[2] == "X" for sublist in TicTacToeArray):
          print("Player One wins!")
          End = True
          break
    #Values are created for the indexs diagonal to each other.
    value1 = TicTacToeArray[0][0]
    value2 = TicTacToeArray[1][1]
    value3 = TicTacToeArray[2][2]
    #When the diagonal indexs are all X, the game is ended, and Player One wins.
    if value1 == "X" and value2 == "X" and value3 == "X":
      print("Player One wins!")
      End = True
      break
    #Values are created for indexs that are diagonal the other way.
    value4 = TicTacToeArray[0][2]
    value5 = TicTacToeArray[1][1]
    value6 = TicTacToeArray[2][0]
    #When these specific indexs are all X, Player One wins.
    if value4 == "X" and value5 == "X" and value6 == "X":
      print("Player One wins!")
      End = True
      break
#The same end conditions are true for player two, and another function is created.
def EndConditionsO():
  #The ending variable must be global here too.
  global End
  #The indexs are enumerated in the 2 dimensional array.
  for index, values in enumerate(TicTacToeArray):
    #If all the values in a row are O, Player Two wins.
    if values[0] == "O" and values[1] == "O" and values[2] == "O":
      print("Player Two wins!")
      #The game is ended.
      End = True
    else:
         #The code checks if all the values in each column are O.
         if all(sublist[0] == "O" for sublist in TicTacToeArray):
          print("Player Two wins!")
          End = True
          #The break prevents the loop from preventing three times.
          break
         elif all(sublist[1] == "O" for sublist in TicTacToeArray):
          print("Player Two wins!")
          End = True
          break
         elif all(sublist[2] == "O" for sublist in TicTacToeArray):
          print("Player Two wins!")
          End = True
          break
    #Values are set for the diagonal indexs again within the function.
    value1 = TicTacToeArray[0][0]
    value2 = TicTacToeArray[1][1]
    value3 = TicTacToeArray[2][2]
    #When the diagonal indexs are all O, Player Two wins.
    if value1 == "O" and value2 == "O" and value3 == "O":
      print("Player Two wins!")
      End = True
      break
    #The same is true for diagonals in both directions.
    value4 = TicTacToeArray[0][2]
    value5 = TicTacToeArray[1][1]
    value6 = TicTacToeArray[2][0]
    if value4 == "O" and value5 == "O" and value6 == "O":
      print("Player Two wins!")
      End = True
      break
#Here is two 2 dimensional board before any pieces are added. There are three sublists within a list.
TicTacToeArray = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
#To print the array, a nested loop prints the values in each row seperately. 
for row in TicTacToeArray:
    for value in row:
        #There is a space after each value.
        print(value, end=" ")
    #The empty print statement ensures that each row is on a seperate line.
    print()
#Instructions are given for the user here.
print("This is the board. No pieces have been placed yet.")
#An array with numbers is given for the user for they know where to place the pieces.
PlacementArray = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
#The Placement array is printed here in the same manner as the board.
for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
#More instructions are given for the user.
print("These are the numbered locations where you can place your piece. Type in a number to place a piece where that number is.")
print("The first player is X and will make the first move.")
#The first player inputs where they will place their first piece.
Placement = input("Choose where you will place your first piece ")
#The input is converted to an integer so it can be compared.
intPlacement = int(Placement)
#A function is created to place the X pieces.
def XPlacement(intPlacement):
 #The placement array is printed each time the user places a piece as a visual representation of where they can place pieces.
 for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
#Here is where a piece can be placed in the upper left corner.
 if intPlacement == 1:
    #A variable is created for the index for the row and column.
    row_index = 0
    column_index = 0
    #Within the array, X is placed with the indexs of the row and column.
    TicTacToeArray[row_index][column_index] = "X"
    #The board is reprinted.
    print("The board is now:")
    for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 #For each placement number, the indexs change, and a placement is created for each index with X.
 elif intPlacement == 2:
   row_index = 0
   #The column index is the first to change with a different placement.
   column_index = 1
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   #The board is printed for every placement.
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 3:
   row_index = 0
   column_index = 2
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 4:
   row_index = 1
   column_index = 0
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 5:
   row_index = 1
   column_index = 1
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 6:
   row_index = 1
   column_index = 2
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 7:
   row_index = 2
   column_index = 0
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 8:
   row_index = 2
   column_index = 1
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 9:
   row_index = 2
   column_index = 2
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
#A function is created to place the O pieces.
def OPlacement(intNextPlacement):
    #The placement array is printed each time the function is called.
  for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
  #The function works in the same way aa the X Placement function, but with O instead of X.
  if intNextPlacement == 1:
    row_index = 0
    column_index = 0
    TicTacToeArray[row_index][column_index] = "O"
    print("The board is now:")
    for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 2:
   row_index = 0
   column_index = 1
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 3:
   row_index = 0
   column_index = 2
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 4:
   row_index = 1
   column_index = 0
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 5:
   row_index = 1
   column_index = 1
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 6:
   row_index = 1
   column_index = 2
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 7:
   row_index = 2
   column_index = 0
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 8:
   row_index = 2
   column_index = 1
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif intNextPlacement == 9:
   row_index = 2
   column_index = 2
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
#The first X piece is placed here.
XPlacement(intPlacement)
#Now, the second player can place their first piece.
print("The next player is O. You can place the next piece based on the board and placement board. Type a number to place your first piece") 
#The O placements have a variable with next so they are more easily distinguished from the X placements.
NextPlacement = input("Choose where you will place your first piece ")
intNextPlacement = int(NextPlacement)
#The piece is only placed if it isn't the same as the previous placement.
if intNextPlacement != intPlacement:
  OPlacement(intNextPlacement)
else:
  #If the user decides to place a piece in the same place, they have to pick another place for it.
  while intNextPlacement == intPlacement:
   print("Invalid input. A piece has already been placed there.")
   #Here the user chooses another location for their piece.
   NextPlacement = input("Reenter where you will put your piece")
   intNextPlacement = int(NextPlacement)
  OPlacement(intNextPlacement)
#Here, Player One can place their second piece.
Placement2 = input("Player One, choose where you will place your second piece ")
intPlacement2 = int(Placement2)
#The places where the user cannot place their piece increase.
if intPlacement2 != intPlacement:
  if intPlacement2 != intNextPlacement:
    #When the place is not taken, the user can place their piece.
    XPlacement(intPlacement2)
  else:
    #Prevented by the loop, the user cannot place their piece in either location that has already been taken.
    while intPlacement2 == intPlacement or intPlacement2 == intNextPlacement:
      #The code prints invalid input until they choose a new piece location.
      print("Invalid input!")
      Placement2 = input("Reenter your piece location!")
      intPlacement2 = int(Placement2)
    #The same conditions in the beginning are used for the user to place their piece.
    if intPlacement2 != intPlacement:
      if intPlacement2 != intNextPlacement:
        XPlacement(intPlacement2)
else:
 #In both circumstances, the user must choose a different location for their piece.
 while intPlacement2 == intPlacement or intPlacement2 == intNextPlacement:
      print("Invalid input!")
      Placement2 = input("Reenter your piece location! ")
      intPlacement2 = int(Placement2)
 if intPlacement2 != intPlacement:
    if intPlacement2 != intNextPlacement:
        XPlacement(intPlacement2)
#The second player can now place their second piece.
print("Player two, you can now place your second piece ")
#The variable includes next, denoting it to O.
NextPlacement2 = input("Choose where you will place your second piece ")
intNextPlacement2 = int(NextPlacement2)
#This time, three places on the board are taken.
if intNextPlacement2 != intNextPlacement:
 if intNextPlacement2 != intPlacement:
   if intNextPlacement2 != intPlacement2:
     OPlacement(intNextPlacement2)
   else: 
     #There are three conditions in the while loop to prevent pieces from getting overwritten.
     while intNextPlacement2 == intPlacement2 or intNextPlacement2 == intPlacement or intNextPlacement2 == intPlacement:
      print("Invalid input that place on the board is already taken")
      #The player must reenter their piece location.
      NextPlacement2 = input("Reenter where you will put your piece ")
      intNextPlacement2 = int(NextPlacement2)
     if intNextPlacement2 != intNextPlacement:
      if intNextPlacement2 != intPlacement:
       if intNextPlacement2 != intPlacement2:
        #The piece is only placed if these conditions are met.
        OPlacement(intNextPlacement2)
 else: 
  #Each time a player tries to enter their piece in a wrong location, they have to reenter it.
  while intNextPlacement2 == intPlacement or intNextPlacement2 == intNextPlacement or intNextPlacement2 == intPlacement2:
      print("Invalid input that place on the board is already taken")
      NextPlacement2 = input("Reenter where you will put your piece ")
      intNextPlacement2 = int(NextPlacement2)
  if intNextPlacement2 != intNextPlacement:
      if intNextPlacement2 != intPlacement:
       if intNextPlacement2 != intPlacement2:
        OPlacement(intNextPlacement2)
else:
   while intNextPlacement2 == intNextPlacement or intNextPlacement2 == intPlacement or intNextPlacement2 == intPlacement2:
      print("Invalid input that place on the board is already taken")
      NextPlacement2 = input("Reenter where you will put your piece ")
      intNextPlacement2 = int(NextPlacement2)
   if intNextPlacement2 != intNextPlacement:
      if intNextPlacement2 != intPlacement:
       if intNextPlacement2 != intPlacement2:
        OPlacement(intNextPlacement2)
Placement3 = input("Player one, choose where you will place your third piece ")
intPlacement3 = int(Placement3)
if intPlacement3 != intNextPlacement:
 if intPlacement3 != intPlacement:
   if intPlacement3 != intPlacement2:
     if intPlacement3 != intNextPlacement2:
       XPlacement(intPlacement3)
       EndConditionsX()
     else:
       while intPlacement3 == intNextPlacement2:
        print("Inavlid input. You can not place a piece there")
        Placement3 = input("Reenter where you will put your piece ")
        intPlacement3 = int(Placement3)
       XPlacement(intPlacement3)
   else: 
     while intPlacement3 == intPlacement2:
        print("Inavlid input. You can not place a piece there")
        Placement3 = input("Reenter where you will put your piece ")
        intPlacement3 = int(Placement3)
     XPlacement(intPlacement3)
 else: 
   while intPlacement3 == intPlacement:
        print("Inavlid input. You can not place a piece there")
        Placement3 = input("Reenter where you will put your piece ")
        intPlacement3 = int(Placement3)
   XPlacement(intPlacement3)
else:
  while intPlacement3 == intNextPlacement:
        print("Inavlid input. You can not place a piece there")
        Placement3 = input("Reenter where you will put your piece ")
        intPlacement3 = int(Placement3)
  XPlacement(intPlacement3)
if not End:
  NextPlacement3 = input("Choose your third placement Player Two ")
  intNextPlacement3 = int(NextPlacement3)
  if intNextPlacement3 != intNextPlacement:
   if intNextPlacement3 != intPlacement:
     if intNextPlacement3 != intPlacement2:
      if intNextPlacement3 != intNextPlacement2:
       if intNextPlacement3 != intPlacement3:
        OPlacement(intNextPlacement3)
        EndConditionsO()
       else:
        while intNextPlacement3 == intPlacement3:
         print("Inavlid input. You can not place a piece there")
         NextPlacement3 = input("Reenter where you will put your piece ")
         intNextPlacement3 = int(NextPlacement3)
        OPlacement(intNextPlacement3)
      else:
       while intNextPlacement3 == intNextPlacement2:
         print("Inavlid input. You can not place a piece there")
         NextPlacement3 = input("Reenter where you will put your piece ")
         intNextPlacement3 = int(NextPlacement3)
       OPlacement(intNextPlacement3)
     else: 
      while intNextPlacement3 == intPlacement2:
         print("Inavlid input. You can not place a piece there")
         NextPlacement3 = input("Reenter where you will put your piece ")
         intNextPlacement3 = int(NextPlacement3)
      OPlacement(intNextPlacement3)
   else: 
    while intNextPlacement3 == intPlacement:
         print("Inavlid input. You can not place a piece there")
         NextPlacement3 = input("Reenter where you will put your piece ")
         intNextPlacement3 = int(NextPlacement3)
    OPlacement(intNextPlacement3)
  else:
   while intNextPlacement3 == intPlacement3:
         print("Inavlid input. You can not place a piece there")
         NextPlacement3 = input("Reenter where you will put your piece ")
         intNextPlacement3 = int(NextPlacement3)
   OPlacement(intNextPlacement3)
if not End:
  Placement4 = input("Choose your fourth Placement, Player One ")
  intPlacement4 = int(Placement4)
  if intPlacement4 != intNextPlacement:
   if intPlacement4 != intPlacement:
     if intPlacement4 != intPlacement2:
      if intPlacement4 != intNextPlacement2:
       if intPlacement4 != intPlacement3:
        if intPlacement4 != intNextPlacement3:
         XPlacement(intPlacement4)
         EndConditionsX()
        else:
         while intPlacement4 == intNextPlacement3:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
          intPlacement4 = int(Placement4)
         XPlacement(intPlacement4)
       else:
        while intPlacement4 == intPlacement3:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
          intPlacement4 = int(Placement4)
        XPlacement(intPlacement4)
      else:
       while intPlacement4 == intNextPlacement2:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
          intPlacement4 = int(Placement4)
       XPlacement(intPlacement4)
     else: 
      while intPlacement4 == intPlacement2:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
          intPlacement4 = int(Placement4)
      XPlacement(intPlacement4)
   else: 
    while intPlacement4 == intPlacement:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
          intPlacement4 = int(Placement4)
    XPlacement(intPlacement4)
  else:
   while intPlacement4 == intNextPlacement:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
          intPlacement4 = int(Placement4)
   XPlacement(intPlacement4)
if not End:
  NextPlacement4 = input("Choose your fourth Placement, Player Two ")
  intNextPlacement4 = int(NextPlacement4)
  if intNextPlacement4 != intNextPlacement:
   if intNextPlacement4 != intPlacement:
     if intNextPlacement4 != intPlacement2:
      if intNextPlacement4 != intNextPlacement2:
       if intNextPlacement4 != intPlacement3:
        if intNextPlacement4 != intNextPlacement3:
         if intNextPlacement != Placement4:
          OPlacement(intNextPlacement4)
          EndConditionsO()
         else:
           print("Inavlid input. You can not place a piece there")
        else:
          print("Inavlid input. You can not place a piece there")
       else:
          print("Inavlid input. You can not place a piece there")
      else:
        print("Inavlid input. You can not place a piece there")
     else:
       print("Inavlid input. You can not place a piece there")
   else: 
      print("Inavlid input. You can not place a piece there")
  else: 
    print("Inavlid input. You can not place a piece there")
if not End:
  Placement5 = input("Choose your last Placement, Player One ")
  intPlacement5 = int(Placement5)
  if intPlacement5 != intNextPlacement:
   if intPlacement5 != intPlacement:
     if intPlacement5 != intPlacement2:
      if intPlacement5 != intNextPlacement2:
       if intPlacement5 != intPlacement3:
        if intPlacement5 != intNextPlacement3:
         if intPlacement5 != intNextPlacement4:
           if Placement5 != Placement4:
            XPlacement(intPlacement5)
            EndConditionsX()
           else:
             print("Inavlid input. You can not place a piece there")
         else:
           print("Inavlid input. You can not place a piece there")
        else:
          print("Inavlid input. You can not place a piece there")
       else:
          print("Inavlid input. You can not place a piece there")
      else:
        print("Inavlid input. You can not place a piece there")
     else:
       print("Inavlid input. You can not place a piece there")
   else: 
      print("Inavlid input. You can not place a piece there")
  else: 
    print("Inavlid input. You can not place a piece there")
if not End:
  print("The Game is a draw!")