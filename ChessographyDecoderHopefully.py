code = input("Input the words: ")
letter = input("What letter would you like to be counted? It is recommended to choose in alphabetical order.")
Count_Letter = code.count(letter)
print(f'The letter count is {Count_Letter}.')
Letter_list = [Count_Letter]
keep_going = True
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
while keep_going is True:
    answer = input("Would you like another letter to be counted? (yes or no)")
    if answer == "yes":
        Loop_letter = input("What letter would you like to be counted?")
        Loop_Count_Letter = code.count(Loop_letter)
        print(f'The letter count is {Loop_Count_Letter}.')
        Letter_list.append(Loop_Count_Letter)
    else:
        keep_going = False
        print(f'The letter counts were {Letter_list}')