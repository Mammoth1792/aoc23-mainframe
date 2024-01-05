# Read in map...backwards :)
map = []
with open("input.txt") as f:
    for line in f:
        row = [*line.strip()]
        # Keep inserting at front of list to build list backwards
        map.insert(0, row) 

still_moving = True
end_row = len(map) - 1
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

total_load = 0
for row_num, row in enumerate(map):
    rock_count = row.count('O')
    total_load += rock_count * (row_num + 1)

print(total_load)