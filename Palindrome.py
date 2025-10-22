#This code determines whether something is a palindrome.
def isPalindrome():
    Inputted_Word = input("Enter a word or sentence")
    #The inputted word is reversed.
    if Inputted_Word== Inputted_Word[::-1]:
      print(f'The string {Inputted_Word} is a palindrome')
    else:
      print(f'The string {Inputted_Word} is not a palindrome')
isPalindrome()