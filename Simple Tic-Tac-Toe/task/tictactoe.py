def check_result(lst):
    sum_of_elem = [sum(i) for i in lst]
    empty_in_lst = list(filter(lambda x: 0 in x, lst))
    if sum(sum_of_elem[:3]) not in range(-1, 2) or 3 in sum_of_elem and -3 in sum_of_elem:
        print("Impossible")
        exit()
    elif 3 in sum_of_elem:
        print("X wins")
    elif -3 in sum_of_elem:
        print("O wins")
    elif any(empty_in_lst):
        print("Game not finished")
    else:
        print("Draw")


inp = input("Enter cells:")
grid = [[i for i in inp[:3]], [i for i in inp[3:6]], [i for i in inp[6:]]]
grid_for_check = grid + \
                 [[grid[j][i] for j in range(3)] for i in range(3)] +\
                 [[grid[0][0], grid[1][1], grid[2][2]]] + \
                 [[grid[0][2], grid[1][1], grid[2][0]]]

grid_exchange = [[1 if i == "X" else -1 if i == "O" else 0 for i in j] for j in grid_for_check]


for i, j in enumerate(grid):
    grid[i] = ["|"] + j + ["|"]
print("---------")
for i in grid:
    print(*i)
print("---------")
check_result(grid_exchange)
