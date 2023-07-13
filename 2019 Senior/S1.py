list_of_num = [[1, 2], [3, 4]]


def horizantal_flip(grid):
    tmp = grid[0][0]
    grid[0][0] = grid[1][0]
    grid[1][0] = tmp

    tmp2 = grid[0][1]
    grid[0][1] = grid[1][1]
    grid[1][1] = tmp2

    return grid

def vertical_flip(grid):
    tmp = grid[0][0]
    grid[0][0] = grid[0][1]
    grid[0][1] = tmp

    tmp2 = grid[1][0]
    grid[1][0] = grid[1][1]
    grid[1][1] = tmp2

    return grid


instructions = input()

for letter in instructions:
    if isinstance(letter, str) is False or letter != "H" and letter != "V":
        print("provide only letters including H and V")
        exit()
    if letter == "H":
        list_of_num = horizantal_flip(list_of_num)
    elif letter == "V":
        list_of_num = vertical_flip(list_of_num)


print(list_of_num)

