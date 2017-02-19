grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

# My solution: first give every 1 a peri of 4; if there is another 1 next to it, reduce the peri by 2(connected land)
class Solution(object):
 def islandPerimeter(self, grid):
  """
  :type grid: List[List[int]]
  :rtype: int
  """
  peri = 0
  for i, row in enumerate(grid):
   for j, element in enumerate(row):
    if element == 1:
     peri += 4
     # left
     if i != 0 and grid[i - 1][j] == 1:
      peri -= 2
     if j != 0 and grid[i][j - 1] == 1:
      peri -= 2
  return peri
