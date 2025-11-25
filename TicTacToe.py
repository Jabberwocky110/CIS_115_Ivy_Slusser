End = False
def EndConditionsX():
 global End
 for index, values in enumerate(TicTacToeArray):
    if values[0] == "X" and values[1] == "X" and values[2] == "X":
      print("Player One wins!")
      End = True
    else:
         if all(sublist[0] == "X" for sublist in TicTacToeArray):
          print("Player One wins!")
          End = True
          break
         elif all(sublist[1] == "X" for sublist in TicTacToeArray):
          print("Player One wins!")
          End = True
          break
         elif all(sublist[2] == "X" for sublist in TicTacToeArray):
          print("Player One wins!")
          End = True
          break
    value1 = TicTacToeArray[0][0]
    value2 = TicTacToeArray[1][1]
    value3 = TicTacToeArray[2][2]
    if value1 == "X" and value2 == "X" and value3 == "X":
      print("Player One wins!")
      End = True
      break
    value4 = TicTacToeArray[0][2]
    value5 = TicTacToeArray[1][1]
    value6 = TicTacToeArray[2][0]
    if value4 == "X" and value5 == "X" and value6 == "X":
      print("Player One wins!")
      End = True
      break
def EndConditionsO():
  global End
  for index, values in enumerate(TicTacToeArray):
    if values[0] == "O" and values[1] == "O" and values[2] == "O":
      print("Player Two wins!")
      End = True
    else:
         if all(sublist[0] == "O" for sublist in TicTacToeArray):
          print("Player Two wins!")
          End = True
          break
         elif all(sublist[1] == "O" for sublist in TicTacToeArray):
          print("Player Two wins!")
          End = True
          break
         elif all(sublist[2] == "O" for sublist in TicTacToeArray):
          print("Player Two wins!")
          End = True
          break
    value1 = TicTacToeArray[0][0]
    value2 = TicTacToeArray[1][1]
    value3 = TicTacToeArray[2][2]
    if value1 == "O" and value2 == "O" and value3 == "O":
      print("Player Two wins!")
      End = True
      break
    value4 = TicTacToeArray[0][2]
    value5 = TicTacToeArray[1][1]
    value6 = TicTacToeArray[2][0]
    if value4 == "O" and value5 == "O" and value6 == "O":
      print("Player Two wins!")
      End = True
      break
TicTacToeArray = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
for row in TicTacToeArray:
    for value in row:
        print(value, end=" ")
    print()
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
XPlacement(intPlacement)
print("The next player is O. You can place the next piece based on the board and placement board. Type a number to place your first piece") 
NextPlacement = input("Choose where you will place your first piece ")
intNextPlacement = int(NextPlacement)
def OPlacement(intNextPlacement):
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
if intNextPlacement != intPlacement:
  OPlacement(intNextPlacement)
else:
  print("Invalid input. A piece has already been placed there.")
Placement2 = input("Choose where you will place your second piece ")
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
