grid = [[8, 9, 10], [16, "X", "X"], [24, "X", 30]]


def check_row(row):
    if row[0] == "X":
        d = (row[-1] - row[1]) / 2
        new_row_val = row[1] - d
        return new_row_val
    if row[1] == "X":
        d = (row[-1] - row[0]) / 2
        new_row_val = row[0] + d
        return new_row_val
    if row[-1] == "X":
        d = (row[1] - row[0]) / 2
        new_row_val = row[0] + d
        return new_row_val


for row_index in range(len(grid)):

    count_X_H = grid[row_index].count("X")
    if "X" in grid[row_index] and count_X_H == 1:
        point = grid[row_index].index("X")
        grid[row_index][point] = int(check_row(grid[row_index]))

    col_list = [col[row_index] for col in grid]
    count_X_V = col_list.count("X")
    if "X" in col_list and count_X_V == 1:
        point = col_list.index("X")
        grid[point][row_index] = int(check_row(col_list))

print(grid)


for col in range(len(grid)):
    col_list = [row[col] for row in grid]
    print(col_list)





# [8, 9, 10],
# [16,'X','X']
# [24, 27, 30]

# (1,2)
#(2,1)