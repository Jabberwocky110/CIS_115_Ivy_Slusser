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
def XPlacement():
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
XPlacement()
print("The next player is O. You can place the next piece based on the board and placement board. Type a number to place your first piece") 
NextPlacement = input("Choose where you will place your first piece ")
intNextPlacement = int(NextPlacement)
def OPlacement():
 if intNextPlacement != intPlacement:
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
 else:
   print("Invalid input. Player One has already placed a piece there")
   return
OPlacement()