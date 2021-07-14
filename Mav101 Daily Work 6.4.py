d1 = float(input("Price of Droid 1: "))
d2 = float(input("Price of Droid 2: "))
d3 = float(input("Price of Droid 3: "))
d4 = float(input("Price of Droid 4: "))
d5 = float(input("Price of Droid 5: "))
d6 = float(input("Price of Droid 6: "))
d7 = float(input("Price of Droid 7: "))
d8 = float(input("Price of Droid 8: "))
d9 = float(input("Price of Droid 9: "))
d10 = float(input("Price of Droid 10: "))
x = input("Week: ")
t = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10
a = t/10

with open("Droid_Cost.txt", 'a') as f:
            print(f"\n\n\nWEEK {x}\n", file=f)

            print(f"Droid 1 cost: ${d1:.2f}\n", file=f)
            print(f"Droid 2 cost: ${d2:.2f}\n", file=f)
            print(f"Droid 3 cost: ${d3:.2f}\n", file=f)
            print(f"Droid 4 cost: ${d4:.2f}\n", file=f)
            print(f"Droid 5 cost: ${d5:.2f}\n", file=f)
            print(f"Droid 6 cost: ${d6:.2f}\n", file=f)
            print(f"Droid 7 cost: ${d7:.2f}\n", file=f)
            print(f"Droid 8 cost: ${d8:.2f}\n", file=f)
            print(f"Droid 9 cost: ${d9:.2f}\n", file=f)
            print(f"Droid 10 cost: ${d10:.2f}\n", file=f)

            print(f"Average Price: ${a:.2f}\n", file=f)
            print(f"Total: ${t:.2f}\n", file=f)