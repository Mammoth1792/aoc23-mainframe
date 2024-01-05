# Read in list of instructions
with open("input.txt") as f:
    for line in f:
        list_of_sequences = line.split(',')

total_value = 0
for sequence in list_of_sequences:
    char_set = [*sequence]
    value = 0
    for char in char_set:
        ascii_value = ord(char)
        value += ascii_value
        value *= 17
        value = value % 256
    total_value += value

print(total_value)