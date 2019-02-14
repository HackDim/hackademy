import random
import Code



def get_empty_grid(size):
    new_grid = []
    for row in range(size):
        new_sublist = []
        for column in range(size):
            new_sublist.append('-')
        new_grid.append(new_sublist)
    return new_grid


def rand_alive():
    number = random.randint(1,50)
    if number == 1:
        return True
    else:
        return False


def fill_grid_random(a_grid,max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        for c_i in range(size):
            if rand_alive() == True:
                remaining = remaining - 1
                if remaining >= 0:
                    a_grid[r_i][c_i] = 'X'
                else:
                    a_grid[r_i][c_i] = '-'
            else:
                    a_grid[r_i][c_i] = '-'
    return a_grid 

def setup_game(size,max_alive):
    a_grid = get_empty_grid(size)
    new_grid = fill_grid_random(a_grid,max_alive)
    return new_grid 






def print_grid(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            print(a_grid[r_i][c_i], end="")
        print("")

print_grid(setup_game(13,5))

    
list_a = [1,2,3,4,5]
list_b = [5,7,8,9,10]

Code.is_duplicate_there(list_a, list_b)

print("Please tell me where your bases are")

print("all your base are now belong to us")

print('lol')