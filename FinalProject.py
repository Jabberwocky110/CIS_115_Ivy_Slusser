#The billing information is kept within a user-defined function.
def billing():
   #Three dictionaries are created for the user's information.
   first_name_dictionary = {
      
   }
   last_name_dictionary = {
      
   }
   billing_dictionary = {
      
   }
   print("Enter your billing/shipping information:")
   #The user inputs all of their information.
   First_Name = input("Enter your first name: ")
   #The first name has its own dictionary so it can be accessed seperately.
   first_name_dictionary["First Name"] = First_Name
   Last_Name = input("Enter your last name: ")
   #The last name is placed in a seperate dictionary.
   last_name_dictionary["Last Name"] = Last_Name
   Address = input("Enter your mailing address: ")
   #All the other information is kept in a general billing dictionary.
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
   #The credit card function is called within the billing function.
   validate_credit_card()
   #Here is where the billing information is printed.
   print("-" * 77)
   #This allows for the spacing to be customized and the wording to be centered.
   space10 = " " * 24
   space9 = "Billing/Shipping Information:"
   #The words and spaces are concatenated into a single variable.
   CatologPrint5 = space10 + space9 + space10
   print(CatologPrint5)
   print("-" * 77)
   #This allows for the lines to be doublespaced. 
   print(" ")
   for key, value in first_name_dictionary.items():
      #Here the end is on a space so that the last name dictionary is printed beside the first name dictionary.
      print(f'{key} {value}', end= " ")
    #The last name dictionary is printed on the same line as the first name dictionary.
   for key, value in last_name_dictionary.items():
      print(f'{key} {value}')
    #The billing dictionary is printed on seperate lines.
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
       #When the credit card is valid, the user can enter the expiration date and CVV number.
       Expiration_Date = input("Enter the expiration date on your card: ")
       CVV = input("Please enter your CVV: ")
    else:
       print("Invalid credit card number entered. Please try again.")
       #By recalling the function, users can enter another credit card number.
       validate_credit_card()
#The product catolog is printed here.
print("-" * 49)
space1 = " " * 17
space2 = "PRODUCT CATALOG"
#Like the other titles, the words are concatenated with the spacing.
space4 = space1 + space2 + space1
print(space4)
print("-" * 49)
#This dictionary contains the catolog numbers as keys without any values.
CatalogNumbers = {
  "1": "",
  "2": "",
  "3": "",
  "4": "",
  "5": ""
}
#This dictionary contains the item names and prices.
Catalog = {
  "USB Drive(128 GB)": "12.00",
  "Mac Book Pro(15 inch)": "2900.00",
  "Arduino 1010(with blue tooth)": "48.00",
  "Ring Camera(wireless)": "156.00",
  "Smart TV(TCL 70 inch)": "359.00"
}
#This dictionary contains the catolog names and quantity of the items.
Quantity_on_Hand = {
   "usb_k981": "1000", 
   "mbpro_490": "45",
   "chip_1010": "325", 
   "cam_78": "98",
   "smt_tv_100": "225"}
#An empty list is created for the lengths of the catolog names.
lengthList = []
#The .keys function enables only the keys in a dictionary to be looped over here.
for key in Catalog.keys():
  #The length for each product title is calculated.
  length = len(key)
  #The length is appended to the empty list.
  lengthList.append(length)
#A new list is created for the lengths subtracted from thirty.
spaceList = []
#Each product title length is looped over.
for value in lengthList:
   #Subtracting the lengths from 30 made the cart look the neatest.
   value3 = int(30 - value)
   #The values are appended to a different list.
   spaceList.append(value3)
CatalogList = []
#Each of the numbers in the list are converted to spaces.
for numbers in spaceList:
   CatologPrint3 = " " * numbers
   CatalogList.append(CatologPrint3)
#The same is done for the catalog SKUs to get the spacing even.
QuantityLength = []
for key in Quantity_on_Hand.keys():
   lengt = len(key)
   QuantityLength.append(lengt)
spacelist2 = []
for value in QuantityLength:
   #11 is one higher than the longest SKU number
   value6 = int(11 - value)
   #There is at least one space between the SKU numbers and the quanities.
   spacelist2.append(value6)
CatalogList2 = []
for numbers in spacelist2:
   CatologPrint5 = " " * numbers
   CatalogList2.append(CatologPrint5)
#Variables are created for specific space lengths.
space5 = " " * 3
space6 = " " * 2
line = "|"
#The variables are combined to customize the catalog print.
CatologPrint = space5 + line + space6
CatologPrint2 = line + space6
#Each of the dictionaries and the list of spaces are combined, using the zip function and items function. This is so the items are printed together and returned without dictionary format.
for (key1, value1), (key2, value2), CatalogList in zip(CatalogNumbers.items(), Catalog.items(), CatalogList):
   #The values for the catalog dictionaries are iterated through and printed on the same lines.
   print(f'{key1}{CatologPrint}{key2}{CatalogList}{CatologPrint2}${value2}')
#The user chooses a product number.
Product = input("Choose a product ID from the product catalog to continue: ")
#The user chooses a quantity.
Quantity = input(f"Enter quantity for product{Product}")
#An empty dictionary is created for the cart.
cart = {
   
}
#The prodcut and its quantity are placed in the cart.
cart[Product] = Quantity
#The user has the option to choose another product.
answer = input("Would you like to add another product(y or n)?" )
if answer == "y":
   Product2 = input("Choose a product ID from the product catalog to continue: ")
   #If the user chooses the same product, the quantity is incremented. 
   if Product2 == Product:
     intQuantity = int(Quantity)
     Quantity = intQuantity + 1
     #The billing function is called because the user is done choosing.
     billing()
   else:
      #A new product is added to the cart with a quantity of one.
      Quantity2 = "1"
      cart[Product2] = Quantity2
      #The billing function is called.
      billing()
if answer == "n":
   reply = input("Are you ready to check out? ")
   if reply == "y":
     #When the user checks out, the billing function is called.
     billing()
print("-" * 77)
space7 = " " * 25
space8 = "Shopping Cart Information"
#The title is centered.
CatologPrint4 = space7 + space8 + space7
print(CatologPrint4)
print("-" * 77)
print("*" * 77)
#The dictionaries, pertaining to the product and the spacing list are zipped.
Zipped = zip(CatalogNumbers.items(), Catalog.items(), Quantity_on_Hand.items(), CatalogList, CatalogList2)
#If the user choose only one item, the item is printed once.
if len(cart) == 1:
 #The product number is converted to an integer.
 ProductNumber = int(Product)
 #The quantity is converted to an integer.
 IntQuantity = int(Quantity)
 #Subtitles with custom spacing after the product descriptions are printed for everything in the cart.
 index = 0
 for values in CatalogList:
  index = index + 1
  if index == ProductNumber:
   print(f"SKU     Quantity   Price     Description{CatalogList}Total")
   print("*" * 77)
 #The catalog is enumerated, which essentially creating indexs for a dictionary in this case.
 for indexs, values in enumerate(Catalog.values()):
    #The index is incremented so the loop will only calculated the total for one item.
    indexs = indexs + 1
    #The loop only calulates the total for the product number the user ordered.
    if indexs == ProductNumber:
     #The values in the catalog dictionary are converted from strings.
     IntValue2 = float(values)
     #The total is calculated by multiplying the quanity by the price.
     total = IntQuantity * IntValue2
 #The zipped dictionary is enumerated with indexs, and each key and value is placed in a pair.
 for index, ((key1, value1), (key2, value2), (key3, value3), CatalogList, CatalogList2) in enumerate(Zipped):
   index = index + 1
   #When the index of the combined dictionary equals the product number, the cart is print.
   if index == ProductNumber:
     #Since the keys and values are paired in the loop, it can print specific keys and values here.
     print(f'{key3}{CatalogList2}{Quantity}     ${value2}     {key2} {CatalogList}${total}')
     print("*" * 77)
     #The cart total is printed.
     print(f"Cart Total: ${total}")
#If the user choose multiple items, the items are iterated through in two seperate loops.
else:
   #The product numbers and quantities are converted to integers.
   ProductNumber1 = int(Product)
   ProductNumber2 = int(Product2)
   IntQuantity1 = int(Quantity)
   IntQuantity2 = int(Quantity2)
   #Subtitles with custom spacing after the product descriptions are printed for everything in the cart.
   index = 0
   for values in CatalogList:
    index = index + 1
    if index == ProductNumber1:
     print(f"SKU     Quantity   Price     Description{CatalogList}     Total")
     print("*" * 77)
   #The catalog values are granted indexs and taked from the catalog dictionary without the keys.
   for index, values in enumerate(Catalog.values()):
      index = index + 1
      #Both products have their total calculated within the loop.
      if index == ProductNumber1:
          IntValue3 = float(values)
          total2 = IntQuantity1 * IntValue3
      if index == ProductNumber2:
         IntValue4 = float(values)
         total3 = IntQuantity2 * IntValue4
    #The zipped dictionary is granted an index and each of the keys and values are iterated through.
   LessZipped = zip(CatalogNumbers.items(), Catalog.items(), Quantity_on_Hand.items())
   ZippedList = zip(CatalogList, CatalogList2)
   for index, ((key1, value1), (key2, value2), (key3, value3)) in enumerate(LessZipped) and (CatalogList, CatalogList2) in enumerate(ZippedList):
        index = index + 1
        #The cart for both products is printed on seperate lines.
        if index == ProductNumber1:
          print(f'{key3}{CatalogList2}{Quantity}{CatalogList}   ${value2}     {key2} {CatalogList}   ${total2}')
        if index == ProductNumber2:
          print(f'{key3}{CatalogList2}{Quantity2}{CatalogList}  ${value2}      {key2} {CatalogList}  ${total3}')
   #The final total is calculated by adding the totals for both items.
   Final_Total = total2 + total3
   print("*" * 77)
   print(f'Cart Total: ${Final_Total}')
