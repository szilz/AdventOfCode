
with open("day4input.txt") as file:
    data = file.read().split("\n")

# part 1
count = 0
for line in data:
    halves = line.split(",")
    first = halves[0].split("-")
    second = halves[1].split("-")
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        count += 1
        # print(first, second)
    elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        count += 1
        # print(first)

print(count)


# part 2
count = 0
for line in data:
    halves = line.split(",")
    first = halves[0].split("-")
    second = halves[1].split("-")
        
    if int(first[1]) >= int(second[0]) and int(second[1]) >= int(first[0]):
        count += 1
        
print(count)