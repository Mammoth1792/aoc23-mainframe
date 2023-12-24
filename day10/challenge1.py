# Read in map
initial_map = []
with open("input.txt") as f:
    for line in f:
        row = [*line.strip()]
        initial_map.append(row)

# Rebuild Map to be X, Y
final_map = []
# Build the X...
for x_pos, row in enumerate(initial_map):
    x = []
    final_map.insert(x_pos, x)
# ...then the Y
for y_pos, row in enumerate(initial_map):
    for x_pos, column in enumerate(row):
        final_map[x_pos].insert(y_pos, column)

start_found = False
start_x = start_y = 0
# Find Starting Position
while not start_found:
    for x, row in enumerate(final_map):
        for y, column in enumerate(row):
            if final_map[x][y] == 'S':
                start_found = True
                start_x = x
                start_y = y
                break
        if start_found:
            break

# Let's begin by going to the right
start_found = False
x = start_x
y = start_y
direction = 'E'
total_moves = 0

while not start_found:
    match direction:
        case 'N':
            y -= 1
        case 'S':
            y += 1
        case 'E':
            x += 1
        case 'W':
            x -= 1
    total_moves += 1
    char = final_map[x][y]
    match char:
        case '|':
            continue
        case '-':
            continue
        case 'L':
            if direction == 'S':
                direction = 'E'
            else:
                direction = 'N'
        case 'J':
            if direction == 'E':
                direction = 'N'
            else:
                direction = 'W'
        case '7':
            if direction == 'E':
                direction = 'S'
            else:
                direction = 'W'
        case 'F':
            if direction == 'N':
                direction = 'E'
            else:
                direction = 'S'
        case 'S':
            start_found = True

print(int(total_moves / 2)) # Dividing in half to find longest point
