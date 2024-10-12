"""
.Synopsis
    Inventory system that is backed by JSON data.
.Description
    Inventory system that reads JSON data to print orders

    1. Prompt the user for input, and indicate they can enter word "quit"
    2. user enters part and then the quantity on two separate lines (two inputs)
    3. check if the order is allowed or not
    4. display error message with appropriate info if part doesn't exist
    4a. Part doesn't exist
    4b. Part exists but not enough quantity
    5. if order is valid, store it and continue
    6. Once the user enters quit, print out an order summary showing:
    6a. part
    6b. number order
    6c. price per part
    6d. grand total at the end
    7. must allow the user to order a part more than once
    8. validate both orders are not exceeding the total amount available
.Author
    James Lewis
.Date
    09/30/2024
"""

supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'


#Your code goes here

#import modules
import json

#load json data
jsonData = json.loads(supplier_data)

#Declare Variables
exitMsg = ["quit"]
exitFlag = False
titleMsg = ["welcome to the parts ordering system, please enter in a part name, followed by quantity",
            "parts for order are:\n "
            "\nsprocket\n"
            "\ngizmo\n"
            "\nwidget\n"
            "\ndodad\n"]

orderMsg = ["please enter in a part name, or quit to exit: ",
            "please enter in a quantity to order: "]
errorMsg = ["error, part doesn't exist, try again",
            "part exists not enough quantity"]
quitMsg = ["your order\n",
           "total: $0\n",
           "thank you for using the parts ordering system!"]
ordInput = ""
qtyInput = ""
ordDict = {"part": "jsonData.get(ordInput)","partQtyOrdered": 0, "pricePerPart": 0, "total": 0}
partValid = False
qtyValid = False

#Start Here
#1. prompt user for input to enter part name / quantity
print(titleMsg[0].capitalize())
print()
print(titleMsg[1].capitalize())


#2. Prompt the user for input, and indicate they can enter word "quit"
ordInput = input(f"\n{orderMsg[0].capitalize()}")
if ordInput.lower() in exitMsg:
    exitFlag = True
    #6. Once the user enters quit, print out an order summary showing:
    #6a. part
    #6b. number order
    #6c. price per part
    #6d. grand total at the end
    print()
    print()
    print(f"{quitMsg[0].capitalize()}")
    print(f"{quitMsg[1].capitalize()}")
    print(f"{quitMsg[2].capitalize()}")


#3. user enters part and then the quantity on two separate lines (two inputs)
#ordInput = input(f"{orderMsg[0]}")
#print(f"{ordInput}")

#3. check if the order is allowed or not
if ordInput.lower() in jsonData["parts"] and ordInput.lower() not in exitMsg:
    partValid = True
elif exitFlag == True:
    print("ignore")
    quit()
else:
    # 4. display error message with appropriate info if part doesn't exist
    partValid = False
    print(f"\n{errorMsg[0].capitalize()}")
    quit()

#4 check part quantity
qtyInput = input(f"\n{orderMsg[1].capitalize()}")
#print(f"{int(qtyInput)}")

#4b. Part exists and is valid but not enough quantity
if ordInput.lower() in jsonData["parts"] and partValid == True:
    # check if quantity of parts is valid / user input matches part / part is valid flag
    if int(qtyInput) <= jsonData["sprocket"]["quantity"] and ordInput.lower() == jsonData["parts"][0] and jsonData["sprocket"]["quantity"] >= 1:
        qtyValid = True
        #update quantity sprocket from jsonData because want to validate if enough quantity available.
        jsonData["sprocket"]["quantity"] -= int(qtyInput)

        #5. if order is valid, store it and continue
        ordDict["part"] = ordInput.lower()
        ordDict["partQtyOrdered"] += int(qtyInput)
        ordDict["pricePerPart"] = jsonData.get(ordInput)["price"]
        ordDict["total"] = ordDict["partQtyOrdered"] * ordDict["pricePerPart"]
        ordDict["total"] = round(ordDict["total"], 3)
    elif int(qtyInput) <= jsonData["dodad"]["quantity"] and ordInput.lower() == jsonData["parts"][3] and jsonData["dodad"]["quantity"] >= 1:
        qtyValid = True
        #update quantity dodad from jsonData because want to validate if enough quantity available.
        jsonData["dodad"]["quantity"] -= int(qtyInput)

        #5. if order is valid, store it and continue
        ordDict["part"] = ordInput.lower()
        ordDict["partQtyOrdered"] += int(qtyInput)
        ordDict["pricePerPart"] = jsonData.get(ordInput)["price"]
        ordDict["total"] = ordDict["partQtyOrdered"] * ordDict["pricePerPart"]
        ordDict["total"] = round(ordDict["total"], 3)
    elif int(qtyInput) <= jsonData["gizmo"]["quantity"] and ordInput.lower() == jsonData["parts"][1] and jsonData["gizmo"]["quantity"] >= 1:
        qtyValid = True
        #update quantity gizmo from jsonData because want to validate if enough quantity available.
        jsonData["gizmo"]["quantity"] -= int(qtyInput)

        #5. if order is valid, store it and continue
        ordDict["part"] = ordInput.lower()
        ordDict["partQtyOrdered"] += int(qtyInput)
        ordDict["pricePerPart"] = jsonData.get(ordInput)["price"]
        ordDict["total"] = ordDict["partQtyOrdered"] * ordDict["pricePerPart"]
        ordDict["total"] = round(ordDict["total"], 3)
    elif int(qtyInput) <= jsonData["widget"]["quantity"] and ordInput.lower() == jsonData["parts"][2] and jsonData["widget"]["quantity"] >= 1:
        qtyValid = True
        #update quantity widget from jsonData because want to validate if enough quantity available.
        jsonData["widget"]["quantity"] -= int(qtyInput)

        #5. if order is valid, store it and continue
        ordDict["part"] = ordInput.lower()
        ordDict["partQtyOrdered"] += int(qtyInput)
        ordDict["pricePerPart"] = jsonData.get(ordInput)["price"]
        ordDict["total"] = ordDict["partQtyOrdered"] * ordDict["pricePerPart"]
        ordDict["total"] = round(ordDict["total"], 3)
    else:
        #print error and mark qty as false
        qtyValid = False
        print(f"\nError, only {jsonData.get(ordInput)["quantity"]} of {ordInput} available!")


#print order summary
if qtyValid == True and partValid == True:
    part = ordDict["part"]
    quantity = ordDict["partQtyOrdered"]
    pricePerPart = ordDict["pricePerPart"]
    total = ordDict["total"]
    print(f"{part} - {quantity} @ {pricePerPart} = {total}")
    print(f"Total: ${total}")
