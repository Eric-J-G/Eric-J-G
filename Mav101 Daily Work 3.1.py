name = input("What is the name of the person you are sending this too? ")
age = input("How old are will they be? ")
bday = input("When is their birthday? ")
sender = input("What is your name?" )

def birthday_greetings():
    print(f"Hello {name},")
    print("")
    print(f"We understand that today, {bday} is your Birthday" + "\n" + "We at MAVRX Inc. would like to wish you a happy birthday")
    print("")
    print(f"Congratulations on turning {age}!!" + "/n" + "Cordially,")
    print(sender)

birthday_greetings()