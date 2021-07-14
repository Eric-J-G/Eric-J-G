import math

def Basel(n):
    x = 1
    sum = 0
    while x <= n:
        sum = sum + 1 / x ** 2
        x = x + 1
    print("Pi = " + str(math.sqrt(sum * 6)))

Basel(int(input("Please input a number: ")))