age = int(input("Please enter your age in years: "))

if age < 13:
    print("You are permitted to view G Rated movies")
    print("Ticket Cost is $1.00")
elif 13 <= age <= 17:
    print("You are permitted to view G Rated and PG-13 movies")
    print("Ticket Cost is $5.00")
elif 18 <= age <= 59:
    print("You are permitted to view any movies")
    print("Ticket Cost is $10.00")
elif age >=60:
    print("You are permitted to view any movies")
    print("Ticket Cost is $3.50")
