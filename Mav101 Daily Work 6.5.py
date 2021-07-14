droid_num = int(input("How many droids did you buy? "))
x = input("Week: ")

droids = list(range(1, droid_num + 1))
a = 0
n = 0
m = 1
j = 1
for x in range(droid_num):
    droids[n] = float(input(f"Price of Droid {j}: "))
    n += 1
    j += 1

total = sum(droids)
avr = total/droid_num

with open("Droid_CostA.txt", 'a') as f: 
    print(f"\n\n\nWEEK {x}\n", file=f)
    for x in range(1, droid_num + 1):
        print(f"Droid {m} cost: ${droids[a]:.2f}\n", file=f)
        m += 1
        a += 1

    print(f"Average Price: ${avr:.2f}\n", file=f)
    print(f"Total: ${total:.2f}\n", file=f)