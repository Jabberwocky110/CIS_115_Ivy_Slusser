print("-" * 55)
space1 = " " * 20
space2 = "PRODUCT CATALOG"
space3 = " " * 20
space4 = space1 + space2 + space3
print(space4)
print("-" * 55)
Catolog = {
  "USB Drive(128 GB)": "$12.00",
  "Mac Book Pro(15 inch)": "$2900.00",
  "Arduino 1010(with blue tooth)": "$48.00",
  "Ring Camera(wireless)": "$156.00",
  "Smart TV(TCL 70 inch)": "$359.00"
}
for values in Catolog:
    length = len(values)
    lengthList = []
    lengthList.append(length)
for value in lengthList:
   spaceList = []
   value2 = 28 - value
   spaceList.append(value)
for numbers in lengthList:
   CatologPrint3 = " " * numbers
countList = []
for count in range(5):
  count1 = count + 1
  countList.append(count1)
space5 = " " * 3
space6 = " " * 2
line = "|"
CatologPrint = space5 + line + space6
CatologPrint2 = line + space6
Keys = Catolog.keys()
Values = Catolog.values()
StringCountList = str(countList)
print(StringCountList, CatologPrint, Keys, CatologPrint3, CatologPrint2, Values)