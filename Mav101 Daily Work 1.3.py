x = input("Call Source Location: ")
y = input("Call Source Destination: ")
z = input("Call Duration in Minutes: ")
Cost = float(z) * .05 + 1.3

print("Call from " + str(x) + " to " + str(y))
print("Duration " + str(z))
print("Cost: $" + str(Cost))