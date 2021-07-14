my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0

#Prints on different Lines
for item in my_list:
    for x in item:
        print(x)
        sum += x

#Prints list on the Same Line
for i in my_list:
        print(*i)
print(f"Sum: {sum}")

print(f"Number of Lists: {len(my_list)}")
print()

numbers = 0

for a in my_list:
    numbers += len(a)

print(f"Number of Numbers: {numbers} ")