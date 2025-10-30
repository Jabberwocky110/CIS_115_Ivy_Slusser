print("-" * 49)
space1 = " " * 17
space2 = "PRODUCT CATALOG"
space3 = " " * 17
space4 = space1 + space2 + space3
print(space4)
print("-" * 49)
CatalogNumbers = {
  "1":"",
  "2": "",
  "3": "",
  "4": "",
  "5": ""
}
Catalog = {
  "USB Drive(128 GB)": "$12.00",
  "Mac Book Pro(15 inch)": "$2900.00",
  "Arduino 1010(with blue tooth)": "$48.00",
  "Ring Camera(wireless)": "$156.00",
  "Smart TV(TCL 70 inch)": "$359.00"
}  
lengthList = []
for key in Catalog.keys():
  length = len(key)
  lengthList.append(length)
spaceList = []
for value in lengthList:
   value3 = int(30 - value)
   spaceList.append(value3)
CatalogList = []
for numbers in spaceList:
   CatologPrint3 = " " * numbers
   CatalogList.append(CatologPrint3)
space5 = " " * 3
space6 = " " * 2
line = "|"
CatologPrint = space5 + line + space6
CatologPrint2 = line + space6
for (key1, value1), (key2, value2), CatalogList in zip(CatalogNumbers.items(), Catalog.items(), CatalogList):
   print(f'{key1}{CatologPrint}{key2}{CatalogList}{CatologPrint2}{value2}')