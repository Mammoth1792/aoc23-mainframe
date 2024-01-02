import itertools as it
range_amount = 999999 # Range amount minus one

## Caution! This takes a VERY long time to run
# Each extra expansion of the galaxy adds a specific number of steps
# So instad, I took that specific number, and multiplied it by one million

# Read in universe...
initial_universe = []
with open("input.txt") as f:
    for line in f:
        row = [*line.strip()]
        initial_universe.append(row)
        #...Expand horizontally if necessary
        if set(row) == {'.'}:
            for _ in range(range_amount):
                initial_universe.append(row)


### Rebuild universe to be X, Y
intermediate_universe = []
final_universe = []

# Build the X...
for count in [*initial_universe[0]]:
    intermediate_universe.append([])

# ...then the Y
for y_pos, row in enumerate(initial_universe):
    y_expand_list = []
    for x_pos, column in enumerate(row):
        intermediate_universe[x_pos].insert(y_pos, column)

#...Expand vertically if necessary
for x, row in enumerate(intermediate_universe):
    final_universe.append(row)
    if set(row) == {'.'}:
        for _ in range(range_amount):
            final_universe.append(row)

galaxy_count = 1
galaxy_num = []
galaxy_positions = {}
## Calculate positions of Galaxies
for x, row in enumerate(final_universe):
    for y, column in enumerate(row):
        if column == '#':
            galaxy_positions[galaxy_count] = {'x': x, 'y': y}
            galaxy_num.append(galaxy_count)
            galaxy_count += 1

# Create list of possible combinations
galaxy_paths = list(it.combinations(galaxy_num, 2))

total_moves = 0
# Calculate Distances
for galaxy in galaxy_paths:
    a = galaxy[0]
    b = galaxy[1]
    abs_x = abs(galaxy_positions[a]['x'] - galaxy_positions[b]['x'])
    abs_y = abs(galaxy_positions[a]['y'] - galaxy_positions[b]['y'])
    total_moves += abs_x + abs_y

print(total_moves)