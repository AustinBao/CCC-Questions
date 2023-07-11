def factor_cords(value):
    factors = []
    for n in range(1, int(value) + 1):
        if int(value) % n == 0:
            factors.append([int(n), int((int(value) / n))])
    return factors


def recursive(grid, row, col, row_max, col_max):
    try:
        leave = True
        if row > row_max and col > col_max:
            print(f"Recursive row=>{row} col=>{col} larger than row or col max)")
            return leave
        else:
            factor_list = factor_cords(grid[row][col])
            print(f"factor_list {factor_list}")
            for factor in factor_list:
                rowIndex = factor[0] - 1
                colIndex = factor[1] - 1
                if rowIndex > row_max or colIndex > col_max:
                    print("Outside grid", rowIndex, colIndex) #mandatory if else continue switch
                    continue
                else:
                    if grid[row_max][col_max] == grid[rowIndex][colIndex]:
                        # mandatory because exit code
                        print(f"Jump to row=>{factor[0]} col=>{factor[1]} value=>{grid[rowIndex][colIndex]}")
                        return "yes" # has to spell right
                    else:
                        # mandatory because you catch logic flow
                        print(f"Factor recursive row=>{factor[0]} col=>{factor[1]} value=>{grid[rowIndex][colIndex]}")
                        return recursive(grid, rowIndex, colIndex, row_max, col_max)

    except Exception as e:
        print("Austin, an error occurred:", str(e))



M = 3
N = 3
'''
grid = []
for row in range(M):
    coordinate = input()
    getdate = coordinate.split(" ")
    if len(getdate) > N:
        print("wrong input length")
        exit()
    grid.append(coordinate.split(" "))
'''
#grid = [[3,2,5],[1,4,5],[9,8,7]] #faster; get right
grid = [[3,2,5],[1,4,5],[30,31,7]] #exception

for row in range(M):
    for col in range(N):
        print(f"Processing row=>{row} col=>{col} value=>{grid[row][col]} rowmax=>{M} colmax=>{N}")
        result = recursive(grid, row, col, M-1, N-1)
        if result == "yes":
            print(result)
            exit()

        if result:
            continue



# print(factor_cords(16))

