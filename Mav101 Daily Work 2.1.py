a = True

x = input("Call Source Location: ")
y = input("Call Source Destination: ")

while a == True:
    z = input("Call Duration in Minutes: ")
    
    if int(z) > 0:
        Cost = "{:.2f}".format(float(z) * .05 + 1.3)

        a = False

    else:
        print("Invalid call duration, please enter again")

print("Call from " + str(x) + " to " + str(y))
print("Duration " + str(z))
print("Cost: $" + str(Cost))