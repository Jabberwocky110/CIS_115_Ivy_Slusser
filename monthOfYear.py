def months_of_year():
   months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   startMonth = int(input("Enter the month you want to start with as a numerical value"))
   endMonth = int(input("Enter the month you want to end with as a numerical value"))
   startMonth = startMonth - 1
   while startMonth < endMonth:
    print(months[startMonth])
    startMonth = startMonth + 1
months_of_year()