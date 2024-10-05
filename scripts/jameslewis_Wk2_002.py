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
	#subTotal.append(float(prices[index]))
	subTotal += [price]
	#subTotal += prices[index]
	print(f"{order.title()} - ${price}")

#print subtotal because customer needs to know total
print(f"\nSubtotal is ${sum(subTotal)}")

#print tax by creating formula to factor in tax
#convert string to percentage in order to be available if tax changes
taxTotal = tax*sum(subTotal)
print(f"Tax {tax * 100}%: ${round(taxTotal, 2)}")

#alternative solution
#tax = 6.25 / 100
#print(f"Tax {tax}%: ${round(taxTotal, 2)}")

#print grand total with everything added together
grandTotal = taxTotal+sum(subTotal)
print(f"Grand Total: ${round(grandTotal, 2)}\n")

#print goodbye message
print(f"\n{restoEndMsg.capitalize()}")


"""
#got this error
Traceback (most recent call last):
  File "E:/projFolderCode/python/jameslewis_Wk2_002.py", line 41, in <module>
    print(f"\nSubtotal is ${sum(price)}")
TypeError: 'float' object is not iterable

Where I believe I made the mistake is, I was expecting price to be a list when it was converted using float().
Clearly that is not the case which is why I made a 2nd list which was empty then appended it.

Traceback (most recent call last):
  File "E:/projFolderCode/python/jameslewis_Wk2_002.py", line 34, in <module>
    subTotal += sum(float([price]))
TypeError: float() argument must be a string or a real number, not 'list'
"""

