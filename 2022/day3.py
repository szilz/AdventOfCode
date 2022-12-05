
with open("day3input.txt") as file:
    items = file.read().split("\n")

# part 1
sum = 0
print(items)

for item in items:
    first_half = item[:int(len(item)/2 + 1)]
    second_half = item[int(len(item)/2 + 1):]
    
    # for letter in first_half:
    #     if letter in second_half:
            
    if 'a' == 'A':
        print("yea")
    if 'a' == 'a':
        print("yea")