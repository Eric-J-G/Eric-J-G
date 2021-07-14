from random import shuffle
l =[]
def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(a <= b for a, b in zip(data, data[1:]))

def bogosort(data) -> list:
    """Shuffle data until sorted."""
    while not is_sorted(data):
        shuffle(data)
    return data
x = 1
while x != 0:
    x = int(input("Please Input a Number: "))
    l.append(x)

print(bogosort(l))