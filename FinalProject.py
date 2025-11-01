def billing():
   first_name_dictionary = {
      
   }
   last_name_dictionary = {
      
   }
   billing_dictionary = {
      
   }
   print("Enter your billing/shipping information:")
   First_Name = input("Enter your first name: ")
   first_name_dictionary["First Name"] = First_Name
   Last_Name = input("Enter your last name: ")
   last_name_dictionary["Last Name"] = Last_Name
   Address = input("Enter your mailing address:" )
   billing_dictionary["Address:"] = Address
   City = input("Enter your city: ")
   billing_dictionary["City:"] = City
   State = input("Enter your state: ")
   billing_dictionary["State:"] = State
   Zip_Code = input("Enter you zip or postal code: ")
   billing_dictionary["Zip/Post Code:"] = Zip_Code
   Email = input("Enter your email address: ")
   billing_dictionary["Email:"] = Email
   Phone = input("Enter your phone number: ")
   billing_dictionary["Phone:"] = Phone
   validate_credit_card()
   print("-" * 77)
   space10 = " " * 24
   space9 = "Billing/Shipping Information:"
   CatologPrint5 = space10 + space9 + space10
   print(CatologPrint5)
   print("-" * 77)
   print(" ")
   for key, value in first_name_dictionary.items():
      print(f'{key} {value}', end= " ")
   for key, value in last_name_dictionary.items():
      print(f'{key} {value}')
   for key, value in billing_dictionary.items():
      print(f'{key} {value}')
#This code checks if a credit card is valid.
def validate_credit_card():
    ccNum = input("Please enter your credit card number ")
    #The number is reversed and assigned to a new variable.
    ccNumReverse = ccNum[::-1]
    cardNumberList = []
    for value in ccNumReverse:
       #Each number in the credit card is placed in a list.
       values = int(value)
       cardNumberList.append(values)
    #The length of the number entered is determined.
    length = len(cardNumberList)
    #Two new lists are created.
    even = []
    odd = []
    count = 0
    #This nested loop enables every other number in the card to be put in a different list.
    while count < length:
     for number in ccNumReverse:
        if count % 2 == 0:
         #The numbers have to be converted to integers again.
         IntNumber = int(number)
         even.append(IntNumber)
         count = count + 1
        else:
          odd.append(number)
          count = count + 1
    #A new list is created when the numbers in one list are multiplied.
    multipliedList = []
    #The numbers in the first list are multiplied by two.
    for num in odd:
        integer = int(num)
        multiplied = (integer * 2)
        multipliedList.append(multiplied)
    NewMultipliedList = []
    #This loop determines if any numbers are greater than nine.
    for Val in multipliedList:
        if Val > 9:
           #For values greater than nine, nine is subtracted from them.
           Val = Val - 9
        NewMultipliedList.append(Val)
    #The two lists are combined to create one list.
    NewcardNumberList = even + NewMultipliedList
    #The values in the combined list are summed. 
    total = sum(NewcardNumberList)
    mod10 = total % 10
    #If the total divied by ten is equal to zero, the code prints valid.
    if mod10 == 0:
       print(f'The credit card number {ccNum} is valid!')
       Expiration_Date = input("Enter the expiration date on your card: ")
       CVV = input("Please enter your CVV: ")
    else:
       print("Invalid credit card number entered. Please try again.")
       #By recalling the function, users can enter another credit card number.
       validate_credit_card()
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
  "USB Drive(128 GB)": "12.00",
  "Mac Book Pro(15 inch)": "2900.00",
  "Arduino 1010(with blue tooth)": "48.00",
  "Ring Camera(wireless)": "156.00",
  "Smart TV(TCL 70 inch)": "359.00"
}
Quantity_on_Hand = {
   "usb_k981": "1000", 
   "mbpro_490": "45",
   "chip_1010": "325", 
   "cam_78": "98",
   "smt_tv_100": "225"}
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
   print(f'{key1}{CatologPrint}{key2}{CatalogList}{CatologPrint2}${value2}')
Product = input("Choose a product ID from the product catalog to continue: ")
Quantity = input(f"Enter quantity for product{Product}")
cart = {
   
}
cart[Product] = Quantity
answer = input("Would you like to add another product(y or n)?" )
if answer == "y":
   Product2 = input("Choose a product ID from the product catalog to continue: ")
   if Product2 == Product:
     intQuantity = int(Quantity)
     Quantity = intQuantity + 1
     billing()
   else:
      Quantity2 = "1"
      cart[Product2] = Quantity2
      billing()
if answer == "n":
   reply = input("Are you ready to check out? ")
   if reply == "y":
     billing()
print("-" * 77)
space7 = " " * 25
space8 = "Shopping Cart Information"
CatologPrint4 = space7 + space8 + space7
print(CatologPrint4)
print("-" * 77)
print("*" * 77)
print("SKU   Quantity   Price      Description               Total    ")
print("*" * 77)
Zipped = zip(CatalogNumbers.items(), Catalog.items(), Quantity_on_Hand.items())
if len(cart) == 1:
 ProductNumber = int(Product)
 IntQuantity = int(Quantity)
 for indexs, values in enumerate(Catalog.values()):
    indexs = indexs + 1
    if indexs == ProductNumber:
     IntValue2 = float(values)
     total = IntQuantity * IntValue2
     break
 for index, ((key1, value1), (key2, value2), (key3, value3)) in enumerate(Zipped):
   index = index + 1
   if index == ProductNumber:
     print(f'{key3}  {Quantity}     ${value2}     {key2}                 {total}')
     print("*" * 77)
     print(f"Cart Total: ${total}")
else:
   ProductNumber1 = int(Product)
   ProductNumber2 = int(Product2)
   IntQuantity1 = int(Quantity)
   IntQuantity2 = int(Quantity2)
   for index, values in enumerate(Catalog.values()):
      index = index + 1
      if index == ProductNumber1:
          IntValue3 = float(values)
          total2 = IntQuantity1 * IntValue3
      if index == ProductNumber2:
         IntValue4 = float(values)
         total3 = IntQuantity2 * IntValue4
   for index, ((key1, value1), (key2, value2), (key3, value3)) in enumerate(Zipped):
       index = index + 1
       if index == ProductNumber1:
          print(f'{key3}  {Quantity}     ${value2}     {key2}           {total2}')
       if index == ProductNumber2:
          print(f'{key3}  {Quantity2}    ${value2}     {key2}            {total3}')
   Final_Total = total2 + total3
   print("*" * 77)
   print(f'Cart Total: ${Final_Total}')