numbers = {
    "Daniel": "555-5555",
    'Anna' : '555-7777',
    'Linus' : '555-6666',
    "Bob" : "555-2222"
}

#Prints name and Number
for key, value in numbers.items():
    print(key)
    print(value)

#Prints Number only
for key, value in numbers.items():
    print(value)

print(f"Length of Dictionary: {len(numbers)}")

#Prints Danial's Info
details = numbers.get("Daniel", 0)
if details:
    print('Contact details: {} {}'.format("Daniel", details))
else:
    print('Contact not found')

#Prints Linus's Number
details = numbers.get("Linus", 0)
if details:
    print("Linus's Numbers: {}".format(details))
else:
    print('Linus not found')

#Prints the Names again for some reason idfk
for key, value in numbers.items():
    print(key)