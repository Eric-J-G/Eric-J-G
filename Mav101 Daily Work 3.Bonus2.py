c = int(input("Please input the power you'd like this range raised to: "))

my_list= range(int(input("Please input the start of your range: ")), int(input("Please input the end of your range: ")) + 1)

def power():
    squares=list(map(lambda x:pow(x,c),my_list))
    for elem in squares:
        print(elem)

print("The value of the numbers in your range raised to the power of " + str(c) + " is:")
power()