def months_of_year():
   startMonth = int(input("Enter the month you want to start with by its number within the year. For example, June: 6"))
   endMonth = int(input("Enter the month you want to end with by its number within the year."))
   months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   for months in range(startMonth, endMonth + 1):
    print(months)
months_of_year()