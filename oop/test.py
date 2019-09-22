import numpy as np

def good_numbers(arr):
    """returns the elements of the matrix"""
    good_nums = []
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            good_nums.append(arr[i,j])
    return good_nums
def get_neighbors_map(mat,valid_starting_digits):
    """ args: (p,q) represents position of bishop currently
     possible moves for knight
     generates a graph(dictionary) that returns the neighbors from elements in mat"""

    from collections import defaultdict
    data = defaultdict(list)
    # X is right/left move, Y is upward downward move
    X = [1,1,2,2,-1,-1,-2,-2]
    Y = [2,-2,1,-1,-2,2,-1,1]
    col_dim = mat.shape[1] - 1
    row_dim = mat.shape[0] - 1
    count = 0
    # valid digits from which a path can be formed
    possible_nums = {k:[] for k in valid_starting_digits}
    for j in valid_starting_digits:
        p,q = np.where(mat==j)
        p,q = p[0],q[0]
        for i in range(len(X)):
            x = p + X[i]
            y = q + Y[i]
            if (x >= 0 and y >= 0) and (x <= row_dim and y <= col_dim) and mat[x,y].isdigit() and j.isdigit():
                possible_nums[j].append(mat[x,y]) 
    return dict([(a,list(map(int,b))) for a,b in possible_nums.items()])

def get_neighbors2(mat,valid_starting_digits):
    """gets neighbors for the bishop"""
    from collections import defaultdict
    data = defaultdict(list)
    # X is right/left move, Y is upward downward move
    x_dim = mat.shape[0] - 1 # gets the total rows
    y_dim = mat.shape[1] - 1 # gets the total columns
    min_shape = min(x_dim,y_dim)
    X = [i for i in range(-min_shape,min_shape+1) for j in range(2) if i != 0]
    Y = [X[i] if i % 2 == 0 else X[i]*-1 for i in range(0,len(X))]
    
    # valid digits from which a path can be formed
    possible_nums = {k:[] for k in valid_starting_digits}
    for j in valid_starting_digits:
        p,q = np.where(mat==j)
        p,q = p[0],q[0]
        for i in range(len(X)):
            x = p + X[i]
            y = q + Y[i]
            if (x >= 0 and y >= 0) and (x <= x_dim and y <= y_dim) and mat[x,y].isdigit() and j.isdigit():
                possible_nums[j].append(mat[x,y]) 
    return dict([(a,list(map(int,b))) for a,b in possible_nums.items()])
def get_neighbors(pos,neighbors_map):
    """returns the neighbors for position given by variable 'pos'"""
    return neighbors_map[pos]
def count(init_pos, num_length,neighbors_map):
    """returns the count of paths as we go through the neighbors"""
    # if only one digit specified, then total is 1
    if num_length == 1: return 1
    # otherwise, count all the paths
    count_of_paths = 0
    for pos in get_neighbors(init_pos,neighbors_map):
        count_of_paths += count(str(pos),num_length-1,neighbors_map)
    return count_of_paths

if __name__ == '__main__':
    type_of = str(input("please enter the type of chess piece: "))
    num_length = int(input("enter number length: "))
    board_rows = int(input("enter board rows"))
    board_cols = int(input("enter board columns"))
    ans = []
    arr = np.empty((0,board_cols), int)


    for i in range(board_rows):
        a = input(f"row {i} entries").split(" ")
        arr = np.append(arr,np.array([a]),axis=0)

    valid_starting_digit  = input("enter 1 valid starting digit")

    if type_of in ['knight','KNIGHT']:
        print("calculating total knight moves")
        # get the elemenets of the matrix arr
        elements_in_matrix = good_numbers(arr)

        # create a mapping dictionary to store key value pairs
        # key is the possible start, values is the next path from key
        neighbors_map = get_neighbors_map(arr, elements_in_matrix)

        # count the total moves made by the knight
        total_knight_moves = count(valid_starting_digit, num_length, neighbors_map)
        print(f"for starting pos: {valid_starting_digit} \
            \n digit_length: {num_length},\notal_knight_moves: {total_knight_moves}")
    else:
        print("calculating bishop moves")
        # bishop moves
        # get the elemenets of the matrix arr
        elements_in_matrix = good_numbers(arr)

        # create a mapping dictionary to store key value pairs
        # key is the possible start, values is the next path from key
        neighbors_map = get_neighbors_map(arr, elements_in_matrix)

        # count the total moves made by the knight
        total_bishop_moves = count(valid_starting_digit, num_length, neighbors_map)
        print(f"for starting pos: {valid_starting_digit} \
            \n digit_length: {num_length},\notal_bishop_moves: {total_bishop_moves}")

