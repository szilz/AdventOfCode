
with open ("day2input.txt") as file:
    directions = file.read().split("\n")

# part 1
x = 0
y = 0
for direction in directions:
    if (direction.startswith("forward")):
        direction = direction.split(" ")
        x += int(direction[1])
    elif (direction.startswith("down")):
        direction = direction.split(" ")
        y += int(direction[1])
    elif (direction.startswith("up")):
        direction = direction.split(" ")
        y -= int(direction[1])
print(x * y)

# part 2
x = 0
y = 0
aim = 0
for direction in directions:
    if direction.startswith("down"):
        direction = direction.split(" ")
        aim += int(direction[1])
    elif direction.startswith("up"):
        direction = direction.split(" ")
        aim -= int(direction[1])
    elif (direction.startswith("forward")):
        direction = direction.split(" ")
        x += int(direction[1])
        y += (int(direction[1]) * aim)
print(x * y)