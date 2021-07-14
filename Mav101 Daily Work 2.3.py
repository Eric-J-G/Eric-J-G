quantity = int(input("How many Travel Pillows would you like to purchase?  "))

while True:
    ps = input("Do you want priority shipping? Type Y for Yes or N for No: ").lower()

    if ps == "y" or ps == "n":
       ps = ps == "y"
       break
if quantity < 11:
    pc = float(quantity) * 21
elif quantity > 10:
    pc = float(quantity) * 15.58

if ps == True:
    sc = quantity * 2 + 60
else:
    sc = float(quantity) * 1.25

print("Product Cost: $" + "{:.2f}".format(float(pc)))
print("Shipping Cost: $" + "{:.2f}".format(float(sc)))
print("Subtotal: $" + "{:.2f}".format(float(sc) + float(pc)))
print("Tax: $" + "{:.2f}".format(float(pc) * .15))
print("Total: $" + "{:.2f}".format(float(pc) * 1.15 + float(sc)))