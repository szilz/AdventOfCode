import os
import sys

with open("day4input.txt") as file:
    bingoBoards = file.read().split("\n")

# empty rows, 2,8,14,20...
numbers_drawn = [int(num) for num in bingoBoards[0].split(",")]

class Board:
    def __init__(self):
        pass

matrix_boards = set()
for i in range(2, len(bingoBoards), 6):
    matrix = [[int(num) for num in bingoBoards[i].split(" ")],
    [int(num) for num in bingoBoards[i + 1].split(" ")],
    [int(num) for num in bingoBoards[i + 2].split(" ")],
    [int(num) for num in bingoBoards[i + 3].split(" ")],
    [int(num) for num in bingoBoards[i + 4].split(" ")]]
    matrix_boards.add(matrix)

# placed_numbers = set()
# for number_drawn in numbers_drawn:
#     placed_numbers.add(number_drawn)
#     for i in range(2, len(bingoBoards)):
#         #if len(placed_numbers) >= 5:
            
         

# for each number drawn
    # put number in placed set
    # traverse each board to locate number
        # check for a bingo if placed >= 5
