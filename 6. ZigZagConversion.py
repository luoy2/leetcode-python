'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

s = "ABC"
numRows = 1
grid = []
for i in range(numRows):
    grid.append([''] * len(s))

cur_row = 0
cur_col = 0
is_zig = False
dir = 1
for character in s:
    print(cur_row, cur_col, character)
    grid[cur_row][cur_col] = character
    if (cur_row == numRows - 1 and dir == 1):
        is_zig = True
        dir *= -1
    elif  (cur_row == 0 and dir == -1):
        is_zig = False
        dir *= -1
    if is_zig:
        cur_col += 1
    if cur_row >=0:
        cur_row += dir # dir ==1: 向下; dir == -1, 向上
    print("next: ", cur_row, cur_col, is_zig)

new_s = []
for i in grid:
    for j in i:
        if j != '':
            new_s.append(j)
''.join(new_s)