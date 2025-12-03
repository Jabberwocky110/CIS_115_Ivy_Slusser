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
          #This ensures that the loop only iterates and prints once.
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
#A function is created to place the X pieces.
def XPlacement(Placement):
 #The placement array is printed each time the user places a piece as a visual representation of where they can place pieces.
 for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
#Here is where a piece can be placed in the upper left corner.
 if Placement == "1":
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
 elif Placement == "2":
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
 elif Placement == "3":
   row_index = 0
   column_index = 2
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   #The board is printed.
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif Placement == "4":
   #Varibales are assigned to the row and column indexes.
   row_index = 1
   column_index = 0
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif Placement == "5":
   row_index = 1
   column_index = 1
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif Placement == "6":
   row_index = 1
   column_index = 2
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif Placement == "7":
   row_index = 2
   column_index = 0
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif Placement == "8":
   row_index = 2
   column_index = 1
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 elif Placement == "9":
   row_index = 2
   column_index = 2
   TicTacToeArray[row_index][column_index] = "X"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
 else:
   print("Invalid input!")
#A function is created to place the O pieces.
def OPlacement(NextPlacement):
    #The placement array is printed each time the function is called.
  for row in PlacementArray:
    for value in row:
        print(value, end=" ")
    print()
  #The function works in the same way aa the X Placement function, but with O instead of X.
  if NextPlacement == "1":
    row_index = 0
    column_index = 0
    TicTacToeArray[row_index][column_index] = "O"
    print("The board is now:")
    for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "2":
   row_index = 0
   column_index = 1
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "3":
   row_index = 0
   column_index = 2
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "4":
   row_index = 1
   column_index = 0
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "5":
   row_index = 1
   column_index = 1
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "6":
   row_index = 1
   column_index = 2
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "7":
   row_index = 2
   column_index = 0
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "8":
   row_index = 2
   column_index = 1
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  elif NextPlacement == "9":
   row_index = 2
   column_index = 2
   TicTacToeArray[row_index][column_index] = "O"
   print("The board is now:")
   for row in TicTacToeArray:
      for value in row:
        print(value, end=" ")
      print()
  else:
    print("Invalid input!")
#The first X piece is placed here.
XPlacement(Placement)
#Now, the second player can place their first piece.
print("The next player is O. You can place the next piece based on the board and placement board. Type a number to place your first piece") 
#The O placements have a variable with next so they are more easily distinguished from the X placements.
NextPlacement = input("Choose where you will place your first piece ")
#The piece is only placed if it isn't the same as the previous placement.
if NextPlacement != Placement:
  OPlacement(NextPlacement)
else:
  #If the user decides to place a piece in the same place, they have to pick another place for it.
  while NextPlacement == Placement:
   print("Invalid input. A piece has already been placed there.")
   #Here the user chooses another location for their piece.
   NextPlacement = input("Reenter where you will put your piece")
  OPlacement(NextPlacement)
#Here, Player One can place their second piece.
Placement2 = input("Player One, choose where you will place your second piece ")
#The places where the user cannot place their piece increase.
if Placement2 != Placement and Placement2 != NextPlacement:
    #When the place is not taken, the user can place their piece.
    XPlacement(Placement2)
else:
 #Prevented by the loop, the user cannot place their piece in either location that has already been taken.
 while Placement2 == Placement or Placement2 == NextPlacement:
      print("Invalid input!")
      Placement2 = input("Reenter your piece location! ")
 #The same conditions in the beginning are used for the user to place their piece.
 if Placement2 != Placement and Placement2 != NextPlacement:
        XPlacement(Placement2)
#The second player can now place their second piece.
print("Player two, you can now place your second piece")
#The variable includes next, denoting it to O.
NextPlacement2 = input("Choose where you will place your second piece ")
#This time, three places on the board are taken.
if NextPlacement2 != NextPlacement and NextPlacement2 != Placement and NextPlacement2 != Placement2:
     OPlacement(NextPlacement2)
else:
#There are three conditions in the while loop to prevent pieces from getting overwritten.
   while NextPlacement2 == NextPlacement or NextPlacement2 == Placement or NextPlacement2 == Placement2:
      print("Invalid input that place on the board is already taken")
      NextPlacement2 = input("Reenter where you will put your piece ")
   if NextPlacement2 != NextPlacement and NextPlacement2 != Placement and NextPlacement2 != Placement2:
        #The piece is only placed if these conditions are met.
        OPlacement(NextPlacement2)
#Here, the first player can enter their thrid piece.
Placement3 = input("Player one, choose where you will place your third piece ")
if Placement3 != NextPlacement and Placement3 != Placement and Placement3 != Placement2 and Placement3 != NextPlacement2:
       XPlacement(Placement3)
       #The end conditions function is called for the first time to check if X wins the game.
       EndConditionsX()
else:
 #More conditions are added to the loop.
 while Placement3 == NextPlacement2 or Placement3 == NextPlacement or Placement3 == Placement2 or Placement3 == Placement:
        print("Inavlid input. You can not place a piece there")
        Placement3 = input("Reenter where you will put your piece ")
        #Players are prevented from replacing the other players pieces.
 if Placement3 != NextPlacement and Placement3 != Placement and Placement3 != Placement2 and Placement3 != NextPlacement2:
             XPlacement(Placement3)
               #The end conditions function is called for the first time to check if X wins the game.
             EndConditionsX()
#The code only continues if the game hasn't been ended.
if not End:
  NextPlacement3 = input("Choose your third placement Player Two ")
  #The conditions are combined into one statement.
  if NextPlacement3 != NextPlacement and NextPlacement3 != Placement and NextPlacement3 != Placement2 and NextPlacement3 != NextPlacement2 and NextPlacement3 != Placement3:
        OPlacement(NextPlacement3)
        EndConditionsO()
  else:
  #Numerous conditions have to be met before the piece can be placed.
   while NextPlacement3 == Placement3 or NextPlacement3 == NextPlacement or NextPlacement3 == Placement2 or NextPlacement3 == NextPlacement2 or NextPlacement3 == Placement:
         print("Inavlid input. You can not place a piece there")
         NextPlacement3 = input("Reenter where you will put your piece ")
   if NextPlacement3 != NextPlacement and NextPlacement3 != Placement and NextPlacement3 != Placement2 and NextPlacement3 != NextPlacement2 and NextPlacement3 != Placement3:
            #The sixth piece is placed now.
            OPlacement(NextPlacement3)
            EndConditionsO()
#This enables the game to stop if a player wins.
if not End:
  Placement4 = input("Choose your fourth Placement, Player One ")
  #Four if statements seems to be the optimal amount of conditions for horizontal spacing even though everything could be condensed into one if else statement.
  if Placement4 != NextPlacement and Placement4 != Placement:
     if Placement4 != Placement2 and Placement4 != NextPlacement2:
       if Placement4 != Placement3:
        if Placement4 != NextPlacement3:
         XPlacement(Placement4)
         EndConditionsX()
        else:
         while Placement4 == NextPlacement3 or Placement4 == Placement3 or Placement4 == NextPlacement2 or Placement4 == Placement2 or Placement4 == NextPlacement or Placement4 == Placement:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
         if Placement4 != NextPlacement and Placement4 != Placement:
          if Placement4 != Placement2 and Placement4 != NextPlacement2:
           if Placement4 != Placement3:
            if Placement4 != NextPlacement3:
             XPlacement(Placement4)
             EndConditionsX()
       else:
        while Placement4 == NextPlacement3 or Placement4 == Placement3 or Placement4 == NextPlacement2 or Placement4 == Placement2 or Placement4 == NextPlacement or Placement4 == Placement:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
        if Placement4 != NextPlacement and Placement4 != Placement:
          if Placement4 != Placement2 and Placement4 != NextPlacement2:
           if Placement4 != Placement3:
            if Placement4 != NextPlacement3:
             XPlacement(Placement4)
             EndConditionsX()
     else:
      while Placement4 == NextPlacement3 or Placement4 == Placement3 or Placement4 == NextPlacement2 or Placement4 == Placement2 or Placement4 == NextPlacement or Placement4 == Placement:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
      if Placement4 != NextPlacement and Placement4 != Placement:
          if Placement4 != Placement2 and Placement4 != NextPlacement2:
           if Placement4 != Placement3:
            if Placement4 != NextPlacement3:
             XPlacement(Placement4)
             EndConditionsX()
  else:
   while Placement4 == NextPlacement3 or Placement4 == Placement3 or Placement4 == NextPlacement2 or Placement4 == Placement2 or Placement4 == NextPlacement or Placement4 == Placement:
          print("Inavlid input. You can not place a piece there")
          Placement4 = input("Reenter where you will put your piece ")
   if Placement4 != NextPlacement and Placement4 != Placement:
          if Placement4 != Placement2 and Placement4 != NextPlacement2:
           if Placement4 != Placement3:
            if Placement4 != NextPlacement3:
             XPlacement(Placement4)
             EndConditionsX()
#The code essentially checks if players are trying to replace each other's pieces between each round.
if not End:
  NextPlacement4 = input("Choose your fourth Placement, Player Two ")
  if NextPlacement4 != NextPlacement and NextPlacement4 != Placement and NextPlacement4 != Placement2 and NextPlacement4 != NextPlacement2:
       if NextPlacement4 != Placement3:
        if NextPlacement4 != NextPlacement3:
         if NextPlacement4 != Placement4:
          OPlacement(NextPlacement4)
          EndConditionsO()
         else:
           while NextPlacement4 == Placement4 or NextPlacement4 == NextPlacement3 or NextPlacement4 == Placement3 or NextPlacement4 == NextPlacement2 or NextPlacement4 == Placement2 or NextPlacement4 == NextPlacement or NextPlacement4 == Placement:
            print("Inavlid input. You can not place a piece there")
            NextPlacement4 = input("Replace your piece, Player Two ")
           if NextPlacement4 != NextPlacement and NextPlacement4 != Placement and NextPlacement4 != Placement2 and NextPlacement4 != NextPlacement2:
            if NextPlacement4 != Placement3:
             if NextPlacement4 != NextPlacement3:
              if NextPlacement4 != Placement4:
               OPlacement(NextPlacement4)
               EndConditionsO()
        else:
         while NextPlacement4 == Placement4 or NextPlacement4 == NextPlacement3 or NextPlacement4 == Placement3 or NextPlacement4 == NextPlacement2 or NextPlacement4 == Placement2 or NextPlacement4 == NextPlacement or NextPlacement4 == Placement:
            print("Inavlid input. You can not place a piece there")
            NextPlacement4 = input("Replace your piece, Player Two ")
         if NextPlacement4 != NextPlacement and NextPlacement4 != Placement and NextPlacement4 != Placement2 and NextPlacement4 != NextPlacement2:
            if NextPlacement4 != Placement3:
             if NextPlacement4 != NextPlacement3:
              if NextPlacement4 != Placement4:
               OPlacement(NextPlacement4)
               EndConditionsO()
       else:
         while NextPlacement4 == Placement4 or NextPlacement4 == NextPlacement3 or NextPlacement4 == Placement3 or NextPlacement4 == NextPlacement2 or NextPlacement4 == Placement2 or NextPlacement4 == NextPlacement or NextPlacement4 == Placement:
            print("Inavlid input. You can not place a piece there")
            NextPlacement4 = input("Replace your piece, Player Two ")
         if NextPlacement4 != NextPlacement and NextPlacement4 != Placement and NextPlacement4 != Placement2 and NextPlacement4 != NextPlacement2:
            if NextPlacement4 != Placement3:
             if NextPlacement4 != NextPlacement3:
              if NextPlacement4 != Placement4:
               OPlacement(NextPlacement4)
               EndConditionsO()
  else: 
    while NextPlacement4 == Placement4 or NextPlacement4 == NextPlacement3 or NextPlacement4 == Placement3 or NextPlacement4 == NextPlacement2 or NextPlacement4 == Placement2 or NextPlacement4 == NextPlacement or NextPlacement4 == Placement:
            print("Inavlid input. You can not place a piece there")
            NextPlacement4 = input("Replace your piece, Player Two ")
            NextPlacement4 = int(NextPlacement4)
    if NextPlacement4 != NextPlacement and NextPlacement4 != Placement and NextPlacement4 != Placement2 and NextPlacement4 != NextPlacement2:
            if NextPlacement4 != Placement3:
             if NextPlacement4 != NextPlacement3:
              if NextPlacement4 != Placement4:
               OPlacement(NextPlacement4)
               EndConditionsO()
if not End:
  Placement5 = input("Choose your last Placement, Player One ")
  if Placement5 != NextPlacement and Placement5 != Placement and Placement5 != Placement2 and Placement5 != NextPlacement2 and Placement5 != Placement3 and Placement5 != NextPlacement3:
         if Placement5 != NextPlacement4:
           if Placement5 != Placement4:
            XPlacement(Placement5)
            EndConditionsX()
           else:
             while Placement5 == NextPlacement4 or Placement5 == Placement4 or Placement5 == NextPlacement3 or Placement5 == Placement3 or Placement5 == NextPlacement2 or Placement5 == Placement2 or Placement5 == NextPlacement or Placement5 == Placement:
               print("Place a piece somewhere else!")
               Placement5 = input("Choose your last Placement, Player One ")
             if Placement5 != NextPlacement and Placement5 != Placement and Placement5 != Placement2 and Placement5 != NextPlacement2 and Placement5 != Placement3 and Placement5 != NextPlacement3:
               if Placement5 != NextPlacement4:
                if Placement5 != Placement4:
                 XPlacement(Placement5)
                 EndConditionsX()
         else:
           while Placement5 == NextPlacement4 or Placement5 == Placement4 or Placement5 == NextPlacement3 or Placement5 == Placement3 or Placement5 == NextPlacement2 or Placement5 == Placement2 or Placement5 == NextPlacement or Placement5 == Placement:
               print("Place a piece somewhere else!")
               Placement5 = input("Choose your last Placement, Player One ")
           if Placement5 != NextPlacement and Placement5 != Placement and Placement5 != Placement2 and Placement5 != NextPlacement2 and Placement5 != Placement3 and Placement5 != NextPlacement3:
               if Placement5 != NextPlacement4:
                if Placement5 != Placement4:
                 XPlacement(Placement5)
                 EndConditionsX()
  else: 
    while Placement5 == NextPlacement4 or Placement5 == Placement4 or Placement5 == NextPlacement3 or Placement5 == Placement3 or Placement5 == NextPlacement2 or Placement5 == Placement2 or Placement5 == NextPlacement or Placement5 == Placement:
               print("Place a piece somewhere else!")
               Placement5 = input("Choose your last Placement, Player One ")
    if Placement5 != NextPlacement and Placement5 != Placement and Placement5 != Placement2 and Placement5 != NextPlacement2 and Placement5 != Placement3 and Placement5 != NextPlacement3:
               if Placement5 != NextPlacement4:
                if Placement5 != Placement4:
                 XPlacement(Placement5)
                 EndConditionsX()
#When nine pieces are on the board, and no one has won, the game is a draw.
if not End:
  print("The Game is a draw!")