def song(start):
    if start < 2:
        print("Invalid Entry")
    while start > 1:
        print(f"{start} bottles of beer on the wall, {start} bottles of beer.Take one down,")
        start = start - 1
        print(f"Take one down, pass it around, {start} bottles of beer on the wall")
        if start == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer" + '\n' + "Take one down, pass it around, no more bottles of beer on the wall!")
            break
        else:
            continue
song(int(input("How many bottles are on the wall? ")))