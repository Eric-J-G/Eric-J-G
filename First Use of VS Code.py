from termcolor import colored
import time
blueKeyCard = False
videoEdu = False
shakey = False
Ach1 = colored('Achievemnt Unlocked: Making a First Impression', 'yellow')
Ach2 = colored('Achievemnt Unlocked: A differnt kind of Handshake', 'yellow')

Items = ["Wallet"]

def inventory():
    print("Press 0 to open your inventory")
    c = int(input())
    if c == 0:
      print("Your Inventory Contains")
      for elem in Items:
          print(elem)


print("What is your name?")
name = input()

print("Hello " + name + ", welcome to your first day here at Genoa Design Internantional.")
time.sleep(1.5)
print("My name is Ruth Ryan and I will be showing you around the offices today.")
time.sleep(1.5)
print("Here is your key card so that you can open certain doors around the office.")
input()

print("She holds out a blue key card")

while blueKeyCard is False:

    print("Press 1 to take the blue key card")
    print("Press 2 to do it poorly")

    inventory()
    
    if c == 1:
        print("You took the card")
        blueKeyCard = True

    elif c == 2:
        print("You trip while trying to grab the card, fall, and look like an idiot.")
        print(Ach1)
        print("But you dust yourself off and take the card")
        blueKeyCard = True

    else:
        print("Try Again")

Items.append("Blue Key Card")

input()
print("You follow Ruth down the hallway, admiring the decor of your new office complex.")
time.sleep(2.5)
print("You notice that all of the rooms have strange names, you see people having a meeting in")
print("'The Bridge' and a room called 'The Crow's Nest', but the door is closed.")
time.sleep(3.5)

print("You arrive at your desk, and it'd pretty awesome. There are 3 monitors, which you have no idea what to do with.")
time.sleep(3)
print("The Space is an open concept, with mant cubicles around the room")

input()
print("'This is great!' you exclaim")
time.sleep(1.5)
print("'I thought you'd like it' Ruth says, with a big smile on her face")
time.sleep(2)

print("She gives you a short tour of the first floor of the complex before returing")
time.sleep(1.5)
print("to your desk and instructs you to watch some introduction videos.")
time.sleep(1.5)
print("She says she has to go attend a meeting, and leaves you alone")
time.sleep(1.5)
print("")

x = 0
caffeine = 0
cup = 0
while videoEdu == False:
    print("What will you do?")
    print("Press 1 to watch the videos")
    print("Press 2 to watch the Browse the files on  your computer")
    if cup > 5:
        print('')
        print("You have " + str(cup) + " cups of coffee on your desk already, and are starting to get wierd looks.")
        print("At least drink one before you get another.")
        print("")
    elif cup <= 5:
        print("Press 3 to watch to go get a coffee")
    
    if cup > 0 and shakey == False:
        print("Press 4 to drink your coffee")

    inventory()
    if c == 1:
        print("You do as you're told, and watch the introduction videos")
        videoEdu = True
    if c == 2:
        x = x + 1
        if x == 1:
            print("You look through the files, but there is nothing interesting")
        else: 
            print("You look through the files, but they are extra not intersting since you already looked at them")
    if c == 3:
        cup = cup + 1
        print("You go get a coffee")
    if c == 4 and cup > 0:
        cup = cup - 1
        caffeine = caffeine + 1
        print("You drink the coffee")
        if caffeine > 7:
            print("Your hands start to shake because you drank 8 cups of coffee, that's enough for you")
            print(Ach2)
            shakey = True

print("")
print("/////////////////////////////////////////////////////")
print("THE END")
print("/////////////////////////////////////////////////////")
print("")