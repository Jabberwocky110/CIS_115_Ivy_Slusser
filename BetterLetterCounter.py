code = input("Input the words: ")
code = code.lower()
def letterCount():
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
 def addCountList():
    for value in countList:
       int(value)
    OverallLetterCount = sum(countList)
    print(OverallLetterCount)
 response = input("Would you like an overall letter count? (Yes or no)")
 if response == "Yes":
    addCountList()
#This function counts the words in a split string and places them is a dictionary.
def word_frequency():
    #The sentence is split on each word.
    code_split = code.split(" ")
    print(f'Here is every word in the sentence: {code_split}')
    WordCount = len(code_split)
    print(f'Your word count is {WordCount}')
    #An empty dictionary is created.
    Word_dictionary = {

    }
    #The words are looped over and counted.
    for key in code_split:
         word_amount = code.count(key)
         #Each word count is placed in the dictionary along with each word.
         Word_dictionary[key] = word_amount
    print(f'The count for each of your words is {Word_dictionary}')
answer = input("Would you like a word count? (Yes or no)")
if answer == "No":
   word_frequency()
Reply = input("Would you like a letter count? (Yes or no)")
if Reply == "Yes":
   letterCount()