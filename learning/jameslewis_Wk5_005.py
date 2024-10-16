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
            "part exists not enough quantity",
            "error, please enter valid quantity number"]
quitMsg = ["your order\n",
           "total: $0\n",
           "thank you for using the parts ordering system!"]
ordInput = ""
qtyInput = ""
ordDict = {"sprocket" : {"partQtyOrdered": 0, "pricePerPart": jsonData.get("sprocket")["price"], "total": 0},
            "gizmo" : {"partQtyOrdered": 0, "pricePerPart": jsonData.get("gizmo")["price"], "total": 0},
            "dodad" : {"partQtyOrdered": 0, "pricePerPart": jsonData.get("dodad")["price"], "total": 0},
            "widget" : {"partQtyOrdered": 0, "pricePerPart": jsonData.get("widget")["price"], "total": 0}
            }
partValid = False
qtyValid = False
ordValid = False
ordTotal = 0

#Start Here
#1. prompt user for input to enter part name / quantity

print(titleMsg[0].capitalize())
print()
print(titleMsg[1].capitalize())
#print(jsonData["sprocket"]["quantity"])


while ordInput.lower() != exitMsg:
    # 2. Prompt the user for input, and indicate they can enter word "quit"
    ordInput = input(f"\n{orderMsg[0].capitalize()}")
    if ordInput.lower() in exitMsg:
        # 6. Once the user enters quit, print out an order summary
        #if qtyValid == True and partValid == True:
        if ordValid == True:
            print()
            print()
            print(f"{quitMsg[0].capitalize()}")

            for part, values in ordDict.items():
                if values["partQtyOrdered"] > 0:
                    qty = values["partQtyOrdered"]
                    pricePerPart = values["pricePerPart"]
                    total = values["total"]
                    ordTotal += values["total"]
                    # 6a. part
                    # 6b. number order
                    # 6c. price per part
                    # 6d. grand total at the end
                    print(f"{part} - {qty} @ {pricePerPart} = {total}\n")

            print(f"Total: ${round(ordTotal,5)}")
            print(f"\n{quitMsg[2].capitalize()}")
            break
        else:
            print()
            print()
            print(f"{quitMsg[0].capitalize()}")
            print(f"{quitMsg[1].capitalize()}")
            print(f"{quitMsg[2].capitalize()}")
            break

    #3. check if the order is allowed or not

    if ordInput.lower() in jsonData["parts"] and ordInput.lower() not in exitMsg:
        partValid = True
        while partValid == True and qtyValid == False:
            qtyInput = input(f"\n{orderMsg[1].capitalize()}")
            if qtyInput.isdigit() != True:
                print(f"\n{errorMsg[2].capitalize()}")
                continue
            else:
                qtyValid = True
                break
    else:
        # 4. display error message with appropriate info if part doesn't exist
        partValid = False
        print(f"\n{errorMsg[0].capitalize()}")

    # 4b. Part exists and is valid but not enough quantity
    if ordInput.lower() in jsonData["parts"] and partValid == True:
        # check if quantity of parts is valid / user input matches part / part is valid flag
        if int(qtyInput) <= jsonData["sprocket"]["quantity"] and ordInput.lower() == jsonData["parts"][0] and jsonData["sprocket"]["quantity"] >= 1:

            if qtyValid == True and partValid == True:
                #mark order valid to store in dictionary
                ordValid = True
                #reset qtyValid flag to get back into while loop to validate quantity
                qtyValid = False

                # update quantity sprocket from jsonData because want to validate if enough quantity available.
                jsonData["sprocket"]["quantity"] -= int(qtyInput)

                # 5. if order is valid, store it and continue
                ordDict[ordInput.lower()]["partQtyOrdered"] += int(qtyInput)
                ordDict[ordInput.lower()]["total"] = ordDict[ordInput.lower()]["partQtyOrdered"] * ordDict[ordInput.lower()]["pricePerPart"]
                ordDict[ordInput.lower()]["total"] = round(ordDict[ordInput.lower()]["total"], 5)

        elif int(qtyInput) <= jsonData["dodad"]["quantity"] and ordInput.lower() == jsonData["parts"][3] and jsonData["dodad"]["quantity"] >= 1:

            if qtyValid == True and partValid == True:
                #mark order valid to store in dictionary
                ordValid = True
                #reset qtyValid flag to get back into while loop to validate quantity
                qtyValid = False

                # update quantity dodad from jsonData because want to validate if enough quantity available.
                jsonData["dodad"]["quantity"] -= int(qtyInput)

                # 5. if order is valid, store it and continue
                ordDict[ordInput.lower()]["partQtyOrdered"] += int(qtyInput)
                ordDict[ordInput.lower()]["total"] = ordDict[ordInput.lower()]["partQtyOrdered"] * ordDict[ordInput.lower()]["pricePerPart"]
                ordDict[ordInput.lower()]["total"] = round(ordDict[ordInput.lower()]["total"], 5)

        elif int(qtyInput) <= jsonData["gizmo"]["quantity"] and ordInput.lower() == jsonData["parts"][1] and jsonData["gizmo"]["quantity"] >= 1:

            if qtyValid == True and partValid == True:
                #mark order valid to store in dictionary
                ordValid = True
                #reset qtyValid flag to get back into while loop to validate quantity
                qtyValid = False

                # update quantity sprocket from jsonData because want to validate if enough quantity available.
                jsonData["gizmo"]["quantity"] -= int(qtyInput)

                # 5. if order is valid, store it and continue
                ordDict[ordInput.lower()]["partQtyOrdered"] += int(qtyInput)
                ordDict[ordInput.lower()]["total"] = ordDict[ordInput.lower()]["partQtyOrdered"] * ordDict[ordInput.lower()]["pricePerPart"]
                ordDict[ordInput.lower()]["total"] = round(ordDict[ordInput.lower()]["total"], 5)

        elif int(qtyInput) <= jsonData["widget"]["quantity"] and ordInput.lower() == jsonData["parts"][2] and jsonData["widget"]["quantity"] >= 1:

            if qtyValid == True and partValid == True:
                #mark order valid to store in dictionary
                ordValid = True
                #reset qtyValid flag to get back into while loop to validate quantity
                qtyValid = False

                # update quantity sprocket from jsonData because want to validate if enough quantity available.
                jsonData["widget"]["quantity"] -= int(qtyInput)

                # 5. if order is valid, store it and continue
                ordDict[ordInput.lower()]["partQtyOrdered"] += int(qtyInput)
                ordDict[ordInput.lower()]["total"] = ordDict[ordInput.lower()]["partQtyOrdered"] * ordDict[ordInput.lower()]["pricePerPart"]
                ordDict[ordInput.lower()]["total"] = round(ordDict[ordInput.lower()]["total"], 5)

        else:
            # print error and mark qty as false
            qtyValid = False
            print(f"\nError, only {jsonData.get(ordInput)["quantity"]} of {ordInput} available!")