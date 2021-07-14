from __future__ import print_function
import time
import sys, select
from msvcrt import kbhit, getwch
import time
import sys
from PIL import Image

print("You walk into work and as you head to your desk a guy calls you over to a side room")
time.sleep(2)
print("'Hey man I gotta run to the bathroom, can you keep an eye on things in here for a minute?'")
time.sleep(2)
print("You look around the room, and the only thing there is a giant contol panel, with a TV screen behind it that displays a view of a small city,")
time.sleep(2)
print("there is only one button, a giant red button in the middle of panel")
time.sleep(2)
print("'What's the button for?' you ask")
time.sleep(2)
print("'Just don't push it' he says, then he leaves")
time.sleep(2)
n = 0
t = 0

def print_flush(*args):
    print(*args, end='')
    sys.stdout.flush()

def timed_input(prompt='', timeout=None):
    if timeout is None:
        return input(prompt)
    print_flush(prompt)
    start = time.time()
    response = ''
    while time.time() - start < timeout:
        if kbhit():
            char = getwch()
            if char == '\r':
                break
            elif char == '\x08': # backspace
                if response:
                    print_flush(char, char)
                    response = response[:-1]
            else:
                print_flush(char)
                response += char
        time.sleep(0.01)
    else:
        response = None
    print()
    return response
end1 = 0
### Test / Demo code:
def main():
    key = ''
    time_limit = 30 # in seconds
    validation = timed_input('Press Enter to push the button: ', time_limit)
    print(validation)
    if validation == key:
        print('You Pushed the Button')
        Push = True
    elif validation is None:
        print('Thanks for keeping an eye on this for me, here, I got you a coffee to say thanks.')
        if end1 == 0:
            end1 += 1
            ending += 1
    else:
        print('ErRoRrr')


ending = 0
end2 = 0

while True:
    main()

    if Push == True:
        print("A new switch appear on the panel")
        time.sleep(1)
        print("Press 1 to flip switch")
        if int(input()) == 1:
            print("Immediatly, the city that was displayed on the screen blows up, leaving a giant mushroom cloud behind")
            if end2 == 0:
                end2 += 1
                ending += 1
