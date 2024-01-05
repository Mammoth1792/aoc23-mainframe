# Read in list of instructions
with open("input.txt") as f:
    for line in f:
        list_of_sequences = line.split(',')

light_boxes = {}
# Build Boxes
for box_num in range(256):
    light_boxes.update({box_num: {}})

for sequence in list_of_sequences:
    char_set = [*sequence]
    box_num = 0
    label = ""
    for char in char_set:
        if char in ['=', '-']:
            if char == '-':
                light_boxes[box_num].pop(label, "No Value")
            else:
                index_num = char_set.index("=")
                lens = char_set[index_num + 1]
                light_boxes[box_num].update({label: lens})
            break
        else: # Calculate box_num
            ascii_value = ord(char)
            box_num += ascii_value
            box_num *= 17
            box_num = box_num % 256
            label += char

total_value = 0
for number, contents in light_boxes.items():
    if len(contents) > 0:
        counter = 1
        lens = list(contents.values())
        for focal_power in lens:
            total_power = (int(number) + 1) * int(focal_power) * counter
            total_value += total_power
            counter += 1

print(total_value)