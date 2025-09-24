#This code caclculates the sales tax for an item
item = float(75.34)

#Print the item price with two decimal places
print(f'The item costs ${item: .2f}')

#Calculate the item with sales tax
item_with_sales_tax = (item * 1.0725)
print(f'The item with sales tax costs ${item_with_sales_tax: .2f}')

#Calculate the sales tax
sales_tax = (item_with_sales_tax - item)
print(f'The sales tax for this item was ${sales_tax: .2f}')
print(f'Your total cost was ${item_with_sales_tax: .2f}')