with open("day2input.txt") as file:
    game = file.read().split("\n")

# part 1
score = 0
for line in game:
    parts = line.split(" ")
    if parts[0] == 'A':
        if parts[1] == 'X':
            score += (1 + 3)
        elif parts[1] == 'Y':
            score += (2 + 6)
        else:
            score += (3 + 0)
    elif parts[0] == 'B':
        if parts[1] == 'X':
            score += (1 + 0)
        elif parts[1] == 'Y':
            score += (2 + 3)
        else:
            score += (3 + 6)
    else:
        if parts[1] == 'X':
            score += (1 + 6)
        elif parts[1] == 'Y':
            score += (2 + 0)
        else:
            score += (3 + 3)
print(score)

# part 2
score = 0
for line in game:
    parts = line.split(" ")
    if parts[0] == 'A': # rock
        if parts[1] == 'X':
            score += (3 + 0)
        elif parts[1] == 'Y':
            score += (1 + 3)
        else:
            score += (2 + 6)
    elif parts[0] == 'B': # paper
        if parts[1] == 'X':
            score += (1 + 0)
        elif parts[1] == 'Y':
            score += (2 + 3)
        else:
            score += (3 + 6)
    else: # scissors
        if parts[1] == 'X':
            score += (2 + 0)
        elif parts[1] == 'Y':
            score += (3 + 3)
        else:
            score += (1 + 6)
print(score)