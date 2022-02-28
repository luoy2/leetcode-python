'''
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

 

Example 1:

Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]

'''

'''
top 0
left 1
right 2
bottom 3
stuck -1
'''

grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
def get_exit(direction_in, corner_dir):
    if direction_in == 0:
        if corner_dir == 1:
            return 2
        else:
            return 1
    elif direction_in == 1:
        if corner_dir == 1:
            return 3
        else:
            return -1
    elif direction_in == 2:
        if corner_dir == 1:
            return -1
        else:
            return 3

def findBallRec(row, col, grid, dir_in):
    if row == len(grid):
        return col
    exit = get_exit(dir_in, grid[row][col])
    if exit == 1:
        if col == 0:
            return -1
        else:
            return findBallRec(row, col-1, grid, 2)
    if exit == 2:
        if col == len(grid[0])-1:
            return -1
        else:
            return findBallRec(row, col+1, grid, 1)
    if exit == -1:
        return -1
    if exit == 3:
        return findBallRec(row+1, col, grid, 0)

def findBall(grid):
    exit = []
    for i in range(len(grid[0])):
        exit.append(findBallRec(0, i, grid, 0))
    return exit

findBall(grid)


# 升级版
exit_map = {}
exit_map[(0, 1)] = 2
exit_map[(0, -1)] = 1
exit_map[(1, 1)] = 3
exit_map[(1, -1)] = -1
exit_map[(2, 1)] = -1
exit_map[(2, -1)] = 3
row_len = len(grid)
col_len = len(grid[0])

def findBallRec(row, col, grid, dir_in, cache_map):
    if row == row_len:
        cache_map[(row, col, dir_in)] = col
    if (row, col, dir_in) not in cache_map:
        exit = exit_map[dir_in, grid[row][col]]
        if exit == 1:
            if col == 0:
                cache_map[(row, col, dir_in)]=-1
            else:
                cache_map[(row, col, dir_in)]=findBallRec(row, col-1, grid, 2, cache_map)
        if exit == 2:
            if col == len(grid[0])-1:
                cache_map[(row, col, dir_in)]=-1
            else:
                cache_map[(row, col, dir_in)]=findBallRec(row, col+1, grid, 1, cache_map)
        if exit == -1:
            cache_map[(row, col, dir_in)]=-1
        if exit == 3:
            cache_map[(row, col, dir_in)]=findBallRec(row+1, col, grid, 0, cache_map)

    return cache_map[(row, col, dir_in)]


def findBall(grid):
    exit = []
    cache_map = {}
    for i in range(len(grid[0])):
        exit.append(findBallRec(0, i, grid, 0, cache_map))
    return exit
findBall(grid)


## 非递归

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n
        for j in range(n):
            col = j  # 球的初始列
            for row in grid:
                dir = row[col]
                col += dir  # 移动球
                if col < 0 or col == n or row[col] != dir:  # 到达侧边或 V 形
                    break
            else:  # 成功到达底部
                ans[j] = col
        return ans

