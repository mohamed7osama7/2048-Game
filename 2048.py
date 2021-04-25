import random

N = 4
GOAL = 1 << (3 * N - 1)
grid = [[0 for i in range(N)] for j in range(N)]


# This function prints the grid of 2048 Game as the game progresses
def print_grid():
    print('-' * ((N + 4) * N + N + 1))
    for i in range(N):
        print(end='|')
        for j in range(N):
            if grid[i][j] == 0:
                e = ' ' * (N + 4)
            else:
                str_len = len(str(grid[i][j]))
                r1 = ((N + 4) - str_len + 1) // 2
                r2 = ((N + 4) - str_len) - r1
                e = (' ' * r1) + str(grid[i][j]) + (' ' * r2)
            print(e, end='|')
        print()
        print('-' * ((N + 4) * N + N + 1))


# This function generates a cell with value 2
def generate_cell():
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    while grid[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    grid[i][j] = 2


# This function rotates the grid by 90 degree anti-clockwise
def rotate_90():
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            k = grid[i][j]
            grid[i][j] = grid[N - j - 1][i]
            grid[N - j - 1][i] = grid[N - i - 1][N - j - 1]
            grid[N - i - 1][N - j - 1] = grid[j][N - i - 1]
            grid[j][N - i - 1] = k


# This function checks if the game state reachs 2048 or not
def check_win():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2048:
                return True
    return False

# This function checks if the current right direction has a movement state or not
def check_available_direction():
    for i in range(0, N):
        for j in range(0, N - 1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0 or grid[i][j] != 0 and grid[i][j + 1] == 0:
                return True

# This function checks if the given direction has a movement state or not
def check_available_move(d):
    res = False
    # check direction right
    if d == 3: res = check_available_direction()
    rotate_90()
    # check direction down
    if d == 5: res = check_available_direction()
    rotate_90()
    # check direction left
    if d == 1: res = check_available_direction()
    rotate_90()
    # check direction up
    if d == 2: res = check_available_direction()
    rotate_90()
    return res


# This function checks if the game has a full state or not
def check_full():
    allgood = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return False

    for i in range(N):
        if grid[i][0] == grid[i][1] or grid[i][1] == grid[i][2] or grid[i][2] == grid[i][3]:
            return False

    for j in range(N):
        if grid[0][j] == grid[1][j] or grid[1][j] == grid[2][j] or grid[2][j] == grid[3][j]:
            return False
    return True


# This function merges the grid with the right direction
def merge():
    for i in range(0, N):
        flag = -1
        counter = 3
        while counter >= 0:
            if grid[i][counter] == 0:
                counter -=1
            else:
                if flag == -1:
                    flag = counter
                else:
                    if grid[i][counter] == grid[i][flag]:
                        grid[i][flag] *= 2
                        grid[i][counter] = 0
                        flag = -1
                    else:
                        flag = counter
                counter -= 1

# This function merges the grid with the given direction
def merge_direction(d):
    # merge direction right
    if d == 3: merge()
    rotate_90()
    # merge direction down
    if d == 5: merge()
    rotate_90()
    # merge direction left
    if d == 1: merge()
    rotate_90()
    # merge direction up
    if d == 2: merge()
    rotate_90()


# This function moves the grid with the left direction
def move():
    for i in range(0, N):
        for j in range(1, N):
            counter = j - 1
            flag = -1
            while counter >= 0:
                if grid[i][counter] == 0:
                    flag = counter
                    counter -= 1
                else:
                    break
            if flag != -1:
                x = grid[i][j]
                grid[i][j] = grid[i][flag]
                grid[i][flag] = x

# This function moves the grid with the given direction
def move_direction(d):
    # move direction left
    if d == 1: move()
    rotate_90()
    # move direction up
    if d == 2: move()
    rotate_90()
    # move direction right
    if d == 3: move()
    rotate_90()
    # move direction down
    if d == 5: move()
    rotate_90()


# This function checks if the given direction is valid or not
def check_valid_direction(i):
    if i == 1 or i == 2 or i == 3 or i == 5:
        return True
    else:
        return False


# This function clears the game structures
def grid_clear():
    for i in range(N):
        for j in range(N):
            grid[i][j] = 0


# This function reads a valid direction
def read_input():
    i = int(input('Enter the direction: '))
    while not check_valid_direction(i) or not check_available_move(i):
        i = int(input('Enter a valid direction: '))
    return i


# MAIN FUNCTION
def play_game():
    print("2048 Game!")
    print("Welcome...")
    print("============================")
    while True:
        # Generate a cell in the grid
        generate_cell()
        # Prints the grid
        print_grid()
        # Check if the state of the grid has a tie state
        if check_full():
            print("Game Over!")
            break
        # Read an input from the player
        i = read_input()
        # Move with the input direction
        move_direction(i)
        # Merge with the input direction
        merge_direction(i)
        # Move with the input direction
        move_direction(i)
        # Check if the grid has a win state
        if check_win():
            # Prints the grid
            print_grid()
            # Announcement of the final statement
            print('Congrats, You won!')
            # Ask for continuing the game
            c = input('Continue [Y/N] ')
            if c not in 'yY':
                break


while True:
    grid_clear()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
