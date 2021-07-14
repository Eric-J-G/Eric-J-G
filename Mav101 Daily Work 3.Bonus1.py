def sum_of(n):

    return sum([x for x in range(0, int(n) + 1) if x % 3 == 0 or x % 5 == 0])

print("The sum of all positive integers up to that point is: " + str(sum_of(int(input("Please input a number: ")))))