pounds, ounces = [float(x) for x in input("Type Weight of Package in Format 'Pounds, Ounces': ").split(", ")]

print(f"Cost is ${(pounds * 16 + ounces) * 0.15}")