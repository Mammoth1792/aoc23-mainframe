# DO NOT RUN THIS
# At 1 million iterations a second, this could take 120 days to complete
from datetime import datetime
startTime = datetime.now()
print("Start Time: " + str(startTime))
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

ending_coordinates_found = False
number_of_steps = 1
while not ending_coordinates_found:
    for direction in list_of_directions:
        for coordinate in starting_locations:
            current_coordinate = starting_locations[coordinate]
            arrived_coordinate = dict_of_coordinates[current_coordinate][direction]
            starting_locations[coordinate] = arrived_coordinate
        all_end_in_z = True
        for coordinate in starting_locations:
            if [*starting_locations[coordinate]][2] != 'Z':
                all_end_in_z = False
                break
        if all_end_in_z:
            ending_coordinates_found = True
            break
        else:
            number_of_steps += 1
print(number_of_steps)
print(datetime.now() - startTime)
print("End Time: " + str(datetime.now()))