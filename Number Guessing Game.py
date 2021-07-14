import random
low = random.randint(1, 500)
high = random.randint(501,1000)
print(f"Pick a number between {low} and {high}. Press Enter to continue")
input()
yn = 0
while yn != "yes":
    guess = random.randrange(low, high, 1)

    while True:
        print(f'Is your number {guess}? ')
        yn = input()

        if yn == "yes" or yn == "no":
            break
    if yn == "yes":
        print("I'm such a good guesser :)")
    else:
        while True:
            H_or_L = input("Higher or Lower?: ").lower()

            if H_or_L == "higher" or H_or_L == "lower":
                if H_or_L == "higher":
                    guess = low
                else:
                    guess = high
                    break