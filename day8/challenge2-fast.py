from math import lcm
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

starting_locations = {}
for coordinate in dict_of_coordinates:
    split_coordinate = [*coordinate]
    if split_coordinate[2] == 'A':
        starting_locations[coordinate] = coordinate

ending_coordinate_found = False
number_of_steps = 1
for coordinate in starting_locations:
    ending_coordinate_found = False
    number_of_steps = 1
    while not ending_coordinate_found:
        for direction in list_of_directions:
            current_coordinate = starting_locations[coordinate]
            arrived_coordinate = dict_of_coordinates[current_coordinate][direction]
            if [*arrived_coordinate][2] == 'Z':
                ending_coordinate_found = True
                break
            else:
                number_of_steps += 1
                starting_locations[coordinate] = arrived_coordinate
    starting_locations[coordinate] = number_of_steps

list_of_nums = []
for coordinate in starting_locations:
    list_of_nums.append(starting_locations[coordinate])


print(lcm(*list_of_nums))