

def possible_dir(row, column, matrix):
    r_limit = len(matrix)
    c_limit = len(matrix[0])
    dirs = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
    valid_dirs = [(row, column) for row, column in dirs if (row >= 0 and row <r_limit) and (column >= 0 and column < c_limit)]
    return valid_dirs


def dfs(r_index, c_index, matrix, visited):
    if (r_index, c_index) not in visited:
        visited.add((r_index, c_index))
        for n_row,n_col in possible_dir(r_index, c_index, matrix):
            if(n_row, n_col) not in visited and matrix[n_row][n_col] != "W":
                dfs(n_row, n_col, matrix, visited)



if __name__ == "__main__":
    grid = [
            ['W', 'W'],
            ['W', 'W'],
            ['W', 'W'],
            ]
    
    row = len(grid)
    column = len(grid[0])
    visited = set()
    count = 0
    
    for row_i in range(row):
        for column_i in range(column):
            if grid[row_i][column_i] == "W":
                continue
            if (row_i, column_i) not in visited:
                count +=1
                dfs(row_i, column_i, grid, visited)
    
    print(count)