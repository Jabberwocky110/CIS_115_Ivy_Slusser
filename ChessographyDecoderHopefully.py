import numpy as np
code = input("Input the words: ")
Letter_dictionary = {
"a":0,
"b":1,
"c":2,
"d": 3,
"e": 4,
"f": 5,
"g": 6,
"h": 7,
"i": 8,
"j": 9,
"k": 10,
"l": 11,
"m": 12,
"n": 13,
"o": 14,
"p": 15,
"q": 16,
"r": 17,
"s": 18,
"t": 19,
"u": 20,
"v": 21,
"w": 22,
"x": 23,
"y": 24,
"z": 25
            }
countList = []
for index, value in enumerate(Letter_dictionary.keys()):
    count = code.count(value)
    countList.append(count)
print(f'{countList}')
Chessboard = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
PossibleInitialletterArray = np.array([["a", "b", "c", "d"], 
                              ["e", "f", "g", "h"], 
                              ["i", "j", "k", "l"],
                              ["m", "n", "o", "p"], 
                              ["r", "s", "t", "u"], 
                              ["v", "w", "x", "y"]])
Pawn = "P"
Rook = "R"
Knight = "N"
Bishop = "B"
Queen = "Q"
King = "K"
#This is the Through the Looking-glass chess game in code.
InitialChessboard = [[0, 0, 0, 0, 0, 0, "N", 0],
                     [0, 0, 0, 0, 0, 0, 0, 0,], 
                     [0, 0, "K", 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, "N", 0, 0],
                     [0, 0, 0, 0, "K", 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, "P", "Q", 0, 0, 0],
                     [0, 0, "Q", 0, 0, "R", 0, 0]]
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
InitialChessboard[6][4] = 0
InitialChessboard[3][7] = "Q"
print("The first move is:")
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("Next")
InitialChessboard[6][3] = 0
InitialChessboard[4][3] = "P"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The white queen moves:")
InitialChessboard[7][2] = 0
InitialChessboard[4][2] = "Q"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
#Here, there is no move so the grid moves forward and stops.
print("The next move is:")
InitialChessboard[4][2] = 0
InitialChessboard[3][2] = "Q"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The pawn moves forward")
InitialChessboard[4][3] = 0
InitialChessboard[3][3] = "P"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The white queen's move into danger:")
InitialChessboard[3][2] = 0
InitialChessboard[0][5] = "Q"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The pawn moves forward:")
InitialChessboard[3][3] = 0
InitialChessboard[2][3] = "P"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("Forest:")
InitialChessboard[2][3] = 0
InitialChessboard[1][3] = "P"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("White queen flies from the red knight:")
InitialChessboard[0][5] = 0
InitialChessboard[0][2] = "Q"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("Check!")
InitialChessboard[0][6] = 0
InitialChessboard[1][4] = "N"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The white knight takes the red knight:")
InitialChessboard[3][5] = 0
InitialChessboard[1][4] = "N"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The white knight returns:")
InitialChessboard[1][4] = 0
InitialChessboard[3][5] = "N"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The pawn advances:")
InitialChessboard[1][3] = 0
InitialChessboard[0][4] = "P"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The red queen moves beside the white queen:")
InitialChessboard[3][7] = 0
InitialChessboard[0][4] = "Q"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("Castling")
InitialChessboard[0][2] = 0
InitialChessboard[2][0] = "Q"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("Alice takes the red queen:")
InitialChessboard[0][3] = 0
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("Checkmate!")
chessography_array = np.array([[0, 0, 0, 0, 0, 0, "N", 0],
                     [0, 0, 0, 0, 0, 0, 0, 0,], 
                     [0, 0, "K", 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, "N", 0, 0],
                     [0, 0, 0, 0, "K", 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, "P", "Q", 0, 0, 0],
                     [0, 0, "Q", 0, 0, "R", 0, 0]])
starting_row = 2
starting_column = 2
end_row = starting_row + PossibleInitialletterArray.shape[0]
end_column = starting_column + PossibleInitialletterArray.shape[1]
chessography_array[starting_row:end_row, starting_column:end_column] = PossibleInitialletterArray
print(chessography_array)
#When no piece moves, does the algorithm capture the location?
Initial_Letters = ["a", "h", "k", "s", "t", "v", "y"]
Next_Letters = ["e", "l", "m", "n", "o"]
PossibleWord = "productions"
EncryptedWord = "jabberwocky"
#Grid moves to capture these letters. The white knight moves to the same place twice (b). It's somehow based on piece arrangement.
nonincludedwords = ["b", "r", "w", "c", "j"]
IncludedLeters = ["a", "k", "y", "e", "o"]