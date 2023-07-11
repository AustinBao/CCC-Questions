def factor_cords(value):
    factors = []
    for n in range(1, int(value) + 1):
        if int(value) % n == 0:
            factors.append([int(n) - 1, int((int(value) / n) - 1)])
    return factors


def recursive(grid, row, col, row_max, col_max):
    try:
        leave = True
        if row == row_max-1 and col == col_max-1:
            return "yes"
        if row > row_max and col > col_max:
            print(row, col, "leave")
            return leave
        else:
            factor_list = factor_cords(grid[row][col])
            print(factor_list)
            for factor in factor_list:
                if factor[0] > row_max or factor[1] > col_max:
                    print("outside grid", [factor[0], factor[1]])
                    continue
                #   return leave
                else:
                    print("jump to", [factor[0], factor[1]])
                    print("value = ", grid[factor[0]][factor[1]])
                    return recursive(grid, factor[0], factor[1], row_max, col_max)

    except Exception as e:
        print("An error occurred:", str(e))



M = 3
N = 3
grid = []
for row in range(M):
    coordinate = input()
    getdate = coordinate.split(" ")
    if len(getdate) > N:
        print("wrong input length")
        exit()
    grid.append(coordinate.split(" "))

print(grid)
print(grid[N-1][M-1])
for row in range(M):
    for col in range(N):
        print(row, col)
        result = recursive(grid, row, col, M, N)
        if result:
            continue
        if result == "yes":
            print(result)


# print(factor_cords(16))
