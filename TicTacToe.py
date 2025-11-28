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
PlacementArray = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
print("These are the locations where you can place your piece. Type in a number to place a piece where that number is.")
print("The first player is X and will make the first move.")
Placement = input("Choose where you will place your first piece ")
intPlacement = int(Placement)
def XPlacement(intPlacement):
 for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
 if intPlacement == 1:
    row_index = 0
    column_index = 0
    TicTacToeArray[row_index][column_index] = "X"
    print("The board is now:")
    for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif intPlacement == 2:
   row_index = 0
   column_index = 1
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
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
def OPlacement(intNextPlacement):
  for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
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
XPlacement(intPlacement)
print("The next player is O. You can place the next piece based on the board and placement board. Type a number to place your first piece") 
NextPlacement = input("Choose where you will place your first piece ")
intNextPlacement = int(NextPlacement)
if intNextPlacement != intPlacement:
  OPlacement(intNextPlacement)
else:
  while intNextPlacement == intPlacement:
   print("Invalid input. A piece has already been placed there.")
   NextPlacement = input("Reenter where you will put your piece")
   intNextPlacement = int(NextPlacement)
  OPlacement(intNextPlacement)
Placement2 = input("Player One, choose where you will place your second piece ")
intPlacement2 = int(Placement2)
if NextPlacement != intPlacement:
  if intPlacement2 != intNextPlacement:
    XPlacement(intPlacement2)
  else:
    print("Invalid input that place on the board is already taken")
else:
  print("Invalid Input. That place on the board is already taken")
print("Player two, you can now place your second piece ")
NextPlacement2 = input("Choose where you will place your second piece ")
intNextPlacement2 = int(NextPlacement2)
if intNextPlacement2 != intNextPlacement:
 if intNextPlacement2 != intPlacement:
   if intNextPlacement2 != intPlacement2:
     OPlacement(intNextPlacement2)
   else: 
     print("Inavlid input. You can not place a piece there")
 else: 
   print("Inavlid input. You can not place a piece there")
else:
  print("Inavlid input. You can not place a piece there")
Placement3 = input("Player one, choose where you will place your third piece ")
intPlacement3 = int(Placement3)
if intPlacement3 != intNextPlacement:
 if intPlacement3 != intPlacement:
   if intPlacement3 != intPlacement2:
     if intPlacement3 != intNextPlacement2:
       XPlacement(intPlacement3)
       EndConditionsX()
     else:
       print("Inavlid input. You can not place a piece there")
   else: 
     print("Inavlid input. You can not place a piece there")
 else: 
   print("Inavlid input. You can not place a piece there")
else:
  print("Inavlid input. You can not place a piece there")
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