
with open ('day1input.txt') as file:
    calories = file.read().split("\n")

# part 1
max_cal = 0 
current_count = 0
for food in calories:
    if food == "":
        current_count = 0
    else:
        current_count += int(food)

    if current_count > max_cal:
        max_cal = current_count

print(max_cal)


# part 2

calorie_count = set()
current_count = 0
for food in calories:
    if food == "":
        calorie_count.add(current_count)
        current_count = 0
    else:
        current_count += int(food)

top_three = 0
for i in range(3):
    num = max(calorie_count)
    top_three += num
    calorie_count.remove(num)

print(top_three)
    