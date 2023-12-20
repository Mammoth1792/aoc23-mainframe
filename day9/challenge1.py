# Read in list of reports
history_reports = []
with open("input.txt") as f:
    for line in f:
        dict_of_sequence = {}
        dict_of_sequence[1] = [int(n) for n in line.split()]
        history_reports.append(dict_of_sequence)

# Calculate All Zeros
for report in history_reports:
    all_zeros = False
    while not all_zeros:
        current_count = len(report)
        next_count = current_count + 1
        new_list = []
        list_counter = 0
        current_set = report[current_count]
        end_counter = len(current_set)
        for values in current_set:
            if list_counter == end_counter - 1:
                break
            else:
                new_list.append((int(current_set[list_counter + 1]) - int(current_set[list_counter])))
                list_counter += 1
        new_list_unique = set(new_list)
        if len(new_list_unique) == 1 and 0 in new_list_unique:
            all_zeros = True
        report[next_count] = new_list

last_number_total = 0
# Build out next iteration
for report in history_reports:
    for count in range(len(report), 0, -1):
        current_set = report[count]
        next_count = count - 1
        next_set = report[next_count]
        new_number = current_set[len(current_set) - 1] + next_set[len(next_set) - 1]
        next_set.append(new_number)
        if next_count == 1:
            last_number_total += new_number
            break

print(last_number_total)