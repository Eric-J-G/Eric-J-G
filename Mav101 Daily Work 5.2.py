en = input("Please Input Employee Number: ")
name = input("Please Input Name: ")
location = input("Please Input Location of Trip: ")
start = input("Please Input Start Date: ")
end = input("Please Input End Date: ")
days = int(input("Length of Trip in Days: "))


if days > 3:
    pd = days * 100
else:
    pd = days * 85

while True:
    car = input("Did you use your own car or a rental? Type O for own or R for rental: ").lower()

    if car == "o" or car == "r":
       car = car == "o"
       break
if car == True:
    km = input("Total Kilometers Travelled: ")
    mileage = float(km) * 0.1
    ca = float(pd) + mileage
else:
    ca = pd

hst = float(pd) * 0.13
ct = ca + hst

print("")
print("")
print(f"Employee Number: {en}")
print(f"Name: {name}")
print(f"Trip Location: {location}")
print(f"Start Date: {start}")
print(f"End Date: {end}")
print(f"Days: {days}")
print(f"Per Diem: ${pd:.2f}")
if car == True:
    print(f"Mileage Amount: ${mileage:.2f}")
print(f"Claim Amount: ${ca:.2f}")
print(f"HST: ${hst:.2f}")
print(f"Claim Total: ${ct:.2f}")
