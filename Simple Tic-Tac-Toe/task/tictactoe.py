def check_result(lst):
    sum_of_elem = [sum(i) for i in lst]
    empty_in_lst = list(filter(lambda x: 0 in x, lst))
    if 3 in sum_of_elem:
        print("X wins")
        return False
    elif -3 in sum_of_elem:
        print("O wins")
        return False
    elif not any(empty_in_lst):
        print("Draw")
        return False
    return True


def check_possibility(user_inp, lst):
    if len(user_inp) != 2:
        print("Enter EXACTLY 2 digits")
        return False
    for i in user_inp:
        if not i.isdigit():
            print("You should enter numbers!")
            return False
        if i not in ("1", "2", "3"):
            print("Coordinates should be from 1 to 3! ")
            return False
    if lst[int(user_inp[0]) - 1][int(user_inp[1]) - 1] != "_":
        print("This cell is occupied! Choose another one!")
        print(lst[int(user_inp[0]) - 1][int(user_inp[1]) - 1])
        return False
    return True


def make_grid(string):
    return [[i for i in string[:3]], [i for i in string[3:6]], [i for i in string[6:]]]


def convert_grid(lst):
    lst_for_check = lst + \
                     [[lst[j][i] for j in range(3)] for i in range(3)] + \
                     [[lst[0][0], lst[1][1], lst[2][2]]] + \
                     [[lst[0][2], lst[1][1], lst[2][0]]]
    return [[1 if i == "X" else -1 if i == "O" else 0 for i in j] for j in lst_for_check]


def print_grid(lst):
    print("---------")
    for i in lst:
        print("|", *i, "|")
    print("---------")


inp = "_________"
grid = make_grid(inp)
print_grid(grid)
flag = 1
while check_result(convert_grid(grid)):
    user_input = input("Enter the coordinates: ").split()
    while not check_possibility(user_input, grid):
        user_input = input("Enter the coordinates: ").split()
    grid[int(user_input[0]) - 1][int(user_input[1]) - 1] = ("Z", "X", "O")[flag]
    flag *= -1
    print_grid(grid)
