
from tkinter import N


with open ("day3input.txt") as file:
    bits = file.read().split("\n")

# part 1
gamma = ""
epsilon = ""
numLength = len(bits[0])
for i in range(numLength):
    numZero = 0
    numOne = 0
    for bit in bits:
        if bit[i] == "0":
            numZero += 1
        else:
            numOne += 1
    if numZero > numOne:
        gamma += "0"
    else:
        gamma += "1"

for bit in gamma:
    if bit == "0":
        epsilon += "1"
    else:
        epsilon += "0"


decGamma = 0
decEpsilon = 0
for i in range(numLength):
    if (gamma[i] == "1"):
        decGamma += pow(2, numLength - 1 - i)
    if (epsilon[i] == "1"):
        decEpsilon += pow(2, numLength - 1 - i)

print(decGamma)
print(decEpsilon)

print(gamma)
print(epsilon)
print(decEpsilon * decGamma)
#print(int(gamma, 2) * int(epsilon, 2))

# part 2
i = 0
def get_most_common(i, numbers, get_common):
    if i == numLength or len(numbers) == 1: # len(numbers) == 1:
        return numbers.pop()
    numOne = set()
    numZero = set()
    for bit_num in numbers:
        if bit_num[i] == "0":
            numZero.add(bit_num)
        else:
            numOne.add(bit_num)
    i += 1
    if len(numOne) >= len(numZero):
        if get_common:# | (get_common == False & i == numLength - 1):
            return get_most_common(i, numOne, True)
        else:
            return get_most_common(i, numZero, False)
    else:
        if get_common:
            return get_most_common(i, numZero, True)
        else:
            return get_most_common(i, numOne, False)

o2_rating = get_most_common(i, bits, True)
co2_rating = get_most_common(i, bits, False)
print(o2_rating)    
print(co2_rating)

def get_decimal(bin_num):
    num = 0
    for i in range(len(bin_num)):
        if (bin_num[i] == "1"):
            num += pow(2, len(bin_num) - 1 - i)
    return num


dec_o2_rating = get_decimal(o2_rating)
dec_co2_rating = get_decimal(co2_rating)

print(dec_o2_rating)    
print(dec_co2_rating)

print(dec_co2_rating * dec_o2_rating)





