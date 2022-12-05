import itertools

with open("day1input.txt") as f:
    lines = f.read().splitlines()

# part 1
total = 0
for line in lines:
    total += int(line)

print(total)

# nico ver

nums = list(map(int, lines))
print(sum(nums))


# part 2

num_set = set()
total2 = 0
has_double = False
while not has_double:
    for line in lines:
        if total2 in num_set:
            print(total2)
            has_double = True
            break
        num_set.add(total2)
        total2 += int(line)

# nico ver

nico_set = {0}
nico_total = 0
for num in itertools.cycle(nums):
    nico_total += num
    if nico_total in nico_set:
        print(nico_total)
        break
    nico_set.add(nico_total)
