import database
import supplier

supplier_database = database.Database()

while True:
    data = input("Enter supplier name, or quit to exit: ")
    if data == "quit":
        break
    s = supplier.Supplier(data)
    print("Part info should be entered in the following format: name, price")
    while True:
        part_info = input("Enter part info, or quit to exit: ")
        if part_info == "quit":
            print()
            break
        try:
            name, price = part_info.split(",")
            price = float(price)
        except:
            print("Error input - Part info should be entered in the following format: name, price - please try again")
            continue
        s.add_part(name, price)
    supplier_database.add_supplier(s)

print("\n\nSupplier database complete!\n")
while True:
    data = input("Please enter in a part name or quit to exit: ")
    if data == "quit":
        break
    
    supplier, price = supplier_database.find_part(data)
    if supplier == False:
        print("Error part does not exist in database")
    else:
        print(f"Part {data} is available for the best price at {supplier}. Price: ${price:.2f}")

print("\nThank you for using the price database!")
