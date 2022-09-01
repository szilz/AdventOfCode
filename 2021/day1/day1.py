
with open("day1input.txt") as file:
    depths = file.read().split("\n")

# part 1
increases = 0
i = 0
for i in range(len(depths)):
    depth = depths[i]
    if depth > depths[i - 1]:
        increases += 1
        
print(increases)

# part 2
increase = 0
for i in range(len(depths) - 2):
    sum = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
    prevSum = int(depths[i-1]) + int(depths[i]) + int(depths[i+1])
    if sum > prevSum:
        increase += 1

print(increase)