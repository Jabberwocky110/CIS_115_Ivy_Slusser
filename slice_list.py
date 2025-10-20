#This code uses a function to slice a list of months.
months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def slice_list():
    months_sliced = months[4:7]
    return months_sliced
months_sliced = slice_list()
print(months_sliced)