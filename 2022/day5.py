
with open("day5ex.txt") as file:
    data = file.readlines()

# part 1
stacks = []
num_stacks = 0
line_count = 0
for line in data:
    parts = line.split()
    line_count += 1
    # found stack count
    if parts[0].isnumeric() == 1:
        num_stacks = len(parts)
        break

# make stacks
for i in range(num_stacks):
    stacks.append([])

for i in range(0, line_count, -1):
    

print(stacks)