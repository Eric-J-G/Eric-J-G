def sum_of(n):
    return sum(range(0, int(n) + 1))

print("The sum of all positive integers up to that point is: " + str(sum_of(int(input("Please input a number: ")))))