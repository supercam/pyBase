"""
.Synopsis
    Creates restoraunt orders and process a receipt
.Description
    contains the following
    1. A restaurant heading
    2. Menu Item and price, one per line
    3. A total
    4. the amount of tax on the order
    5. A grand total including tax
    6. A goodbye message
.Author
    James Lewis
.Date
    09/09/2024
"""

#Declare Variables
orders = ["pepperoni", "cheese", "spicy meats", "hawaiian", "supreme"]
prices = ["5.99", "4.99", "7.99", "8.99", "6.99"]
subTotal = []
exitMsg = "Thank you for dining with us! Hope to see you again!"
restoHeader = "the italian pizza company receipt\n"
restoEndMsg = "thank you for dining with us! we hope to see you soon!"
tax = 0.0625

#print receipt because header needed
print(f"{restoHeader.title()}\n")

#print menu item and price per line in order to notify customer of itemized order
for index in range(len(orders)):
	order = orders[index]
	price = float(prices[index])
	subTotal.append(float(prices[index]))
	print(f"{order.title()} - ${price}")


#print subtotal because customer needs to know total
print(f"\nSubtotal is ${sum(subTotal)}")

#print tax by creating formula to factor in tax
#convert string to percentage in order to be available if tax changes
taxTotal = tax*sum(subTotal)
print(f"Tax {tax:.2%}: ${round(taxTotal, 2)}")

#print grand total with everything added together
grandTotal = taxTotal+sum(subTotal)
print(f"Grand Total: ${round(grandTotal, 2)}\n")

#print goodbye message
print(f"\n{restoEndMsg.capitalize()}")

