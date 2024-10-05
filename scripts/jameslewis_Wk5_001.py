"""
.Synopsis
    Inventory system that is backed by JSON data.
.Description
    Inventory system that reads JSON data to print orders

    6. Prompt the user for input, and indicate they can enter word "quit"
    7. user enters part and then the quantity on two separate lines (two inputs)
    8. check if the order is allowed or not
    9. display error message with appropriate info if part doesn't exist
    9a. Part doesn't exist
    9b. Part exists but not enough quantity
    10. if order is valid, store it and continue
    11. Once the user enters quit, print out an order summary showing:
    11a. part
    11b. number orderd
    11c. price per part
    11d. grand total at the end
    12. Order data must be stored in a dictionary
    13. must allow the user to order a part more than once
    14. validate both orders are not exceeding the total amount available
    15. must store user's order in a dictionary
.Author
    James Lewis
.Date
    09/30/2024
"""

#Declare Variables

#ordInput = input()
#ordInput = input()
exitMsg = ["quit"]
orderAllowed = True
titleMsg = ["welcome to the parts ordering system, please enter in a part name, followed by quantity",
            "parts for order are:\n "
            "\nsprocket\n"
            "\ngizmo\n"
            "\nwidget\n"
            "\ndodad"]
errorMsg = ["part doesn't exist",
            "part exists not enough quanity"]
orderData = ""




print(titleMsg[0])
print(titleMsg[1])
