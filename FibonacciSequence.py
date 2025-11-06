#This prints the Fibonacci Sequence.
Number = 0
NextNumber = 1
NumberList = [0, 1]
for value in range(46):
   NewNumber = Number + NextNumber
   NumberList.append(NewNumber)
   Number = NextNumber
   NextNumber = NewNumber
print(NumberList)
#Here are other versions of the Fibonacci Sequence.
Number2 = 2
NextNumber2 = 3
NumberList2 = [2, 3]
for value2 in range(46):
   NewNumber2 = Number2