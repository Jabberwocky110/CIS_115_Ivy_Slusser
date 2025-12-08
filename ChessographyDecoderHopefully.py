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
PossibleInitialletterArray = [["a", "b", "c", "d"], 
                              ["e", "f", "g", "h"], 
                              ["i", "j", "k", "l"],
                              ["m", "n", "o", "p"], 
                              ["r", "s", "t", "u"], 
                              ["v", "w", "x", "y"]]
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
print("The next move is:")
InitialChessboard[4][2] = 0
InitialChessboard[3][2] = "Q"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The pawn moves forward")
InitialChessboard[4][3] = 0
InitialChessboard[4][2] = "P"
for rows in InitialChessboard:
    for value in rows:
        print(value, end = " ")
    print()
print("The white queen's move into danger:")
InitialChessboard[3][2] = 0
InitialChessboard[0][5] = "Q"