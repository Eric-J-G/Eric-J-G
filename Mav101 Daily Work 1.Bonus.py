x = input("Enter Customer's Name: ")
cost_of_parts = float(input("Type cost of parts: "))
cost_of_labor = (float(input("Input hours of Labor: "))) * 35
subtotal = cost_of_parts + cost_of_labor

print("Name: " + x)
print("Subtotal is $" + str(subtotal))
print("HST is $" + str(cost_of_parts * .15))
print("Total Cost is $" + str(subtotal * 1.15))