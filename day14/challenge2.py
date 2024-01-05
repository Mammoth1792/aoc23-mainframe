# Function to flip array counter-clockwise (since it's already upside down)
def flip_map(map):
    new_map = []
    count = 0
    for _ in map:
        new_row = [item[count] for item in map] # Thank you StackExchange
        new_map.insert(0, new_row)
        count += 1
    return new_map

# Read in map...backwards :)
map = []
cycle_count = 1000 ## Not sure why, but you only need to run it 1,000 times?
with open("input.txt") as f:
    for line in f:
        row = [*line.strip()]
        # Keep inserting at front of list to build list backwards
        map.insert(0, row) 

still_moving = True
end_row = len(map) - 1
for cycle in range(cycle_count):
    for turn in range(4):
        while still_moving:
            still_moving = False
            for row_num, row in enumerate(map):
                if row_num == end_row: continue
                if 'O' in row:
                    for icon_num, icon in enumerate(row):
                        if icon == 'O':
                            next_row_num = row_num + 1
                            if map[next_row_num][icon_num] == '.':
                                map[row_num][icon_num] = '.'
                                map[next_row_num][icon_num] = 'O'
                                still_moving = True
        map = flip_map(map)
        still_moving = True

total_load = 0
for row_num, row in enumerate(map):
    rock_count = row.count('O')
    total_load += rock_count * (row_num + 1)

print(total_load)