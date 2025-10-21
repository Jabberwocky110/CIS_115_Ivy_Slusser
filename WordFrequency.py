#This function counts the words in a split string and places them is a dictionary.
def word_frequency():
    sentence = input("Enter the sentence with the words you want to count")
    #The sentence is split on each word.
    sentence_split = sentence.split(" ")
    print(f'Here is every word in the sentence: {sentence_split}')
    #An empty dictionary is created.
    Word_dictionary = {

    }
    #The words are looped over and counted.
    for key in sentence_split:
         word_amount = sentence_split.count(key)
         #Each word count is placed in the dictionary along with each word.
         Word_dictionary[key] = word_amount
    print(f'The count for each of your word is {Word_dictionary}')
word_frequency()