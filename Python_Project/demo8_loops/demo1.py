# print 1 to 10

# for a in range(1,11):
#     print(a)


colors = ["red", "green", "yellow", "blue", "green", "black", "grey"]

for i in range(0, len(colors)):
    print(colors[i])

numbers = [45, 98, 75, 65, 24, 88, 74, 56, 75]

# print all item that are less than or equal to 50
for i in range(0,len(numbers)):
    if numbers[i]==24:
        print(numbers[i])
        break


for i in range(0,len(numbers)):
    if numbers[i]==24:
        continue
    print(numbers[i])