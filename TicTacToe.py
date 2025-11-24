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
Placement = input("Choose where you will place your first piece")
intPlacement = int(Placement)
if intPlacement == 1:
    row_index = 1
    column_index = 1
    Replacement = "X"
    TicTacToeArray[row_index][column_index] = Replacement
