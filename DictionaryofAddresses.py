#This code enables a user to print specific values from multiple dictionaries within a list.
names_and_addresses = [
    {"firstName": "Anna",
     "lastName": "Barns",
     "city": "Montgomery",
     "state": "Alambama",
     "zipCode": "12121",
     "phoneNumber": "121-212-1212"
     },

     {"firstName": "Cedric",
      "lastName": "Davis",
      "city": "Claymont",
      "state": "Delaware",
      "zipCode": "34343",
      "phoneNumber": "343-434-3434"
     },

    {"firstName": "Eric", 
     "lastName": "FitzRoy",
     "city": "Miami",
     "state": "Florida",
     "zipCode": "565656",
     "phoneNumber": "565-656-5656"
     }
]
def print_dictionary():
    #The user inputs the key for the values they want to print.
    key = input("Enter what you want to print")
    #The loop iterates through each dictionary in the array and prints the user-defined values.
    for value in names_and_addresses:
       item = value[key]
       print(item)
print_dictionary()