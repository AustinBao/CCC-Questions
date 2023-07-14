positions = "BABBCACC"
swap_counter = 0

count = {}
for letters in positions:
    if letters not in count:
        count[letters] = 1
    else:
        count[letters] += 1

print(count)

max_a = []
max_b = []
max_c = []

for curr_letter in count:
    width = count[curr_letter]

    for start_index in range(len(positions)):
        new_lst = positions[start_index:start_index + width]

        if curr_letter == "A":
            if new_lst.count(curr_letter) > max_a.count(curr_letter):
                max_a = new_lst
        if curr_letter == "B":
            if new_lst.count(curr_letter) > max_b.count(curr_letter):
                max_b = new_lst
        if curr_letter == "C":
            if new_lst.count(curr_letter) > max_c.count(curr_letter):
                max_c = new_lst

        start_index += 1

    #trying to remove the already used substrings (no clue how though without start_index)
    positions = positions[:start_index + width] + positions[start_index + width:]


print(max_b, max_a, max_c)
