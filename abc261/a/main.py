input = input()

numbers = input.split(sep=" ")

L1 = int(numbers[0])
R1 = int(numbers[1])
L2 = int(numbers[2])
R2 = int(numbers[3])

print(max(0, min(R1, R2) - max(L1, L2)))
