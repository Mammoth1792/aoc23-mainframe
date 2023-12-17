# Read in list of directions
with open("directions.txt") as f:
    for line in f:
        list_of_directions = [*line]

# Read in list of coordinates
dict_of_coordinates = {}
with open("coordinates.txt") as f:
    for line in f:
       line = line.strip()
       (key, values) = line.split(" = ")
       values = values.strip("()")
       (left, right) = values.split(", ")
       coordinates = {}
       coordinates['L'] = left
       coordinates['R'] = right
       dict_of_coordinates[key] = coordinates

coordinate_key = 'AAA'
ending_coordinate_found = False
number_of_steps = 1
while not ending_coordinate_found:
    for direction in list_of_directions:
        arrived_coordinate = dict_of_coordinates[coordinate_key][direction]
        if arrived_coordinate == 'ZZZ':
            ending_coordinate_found = True
            break
        else:
            number_of_steps += 1
            coordinate_key = arrived_coordinate
print(number_of_steps)