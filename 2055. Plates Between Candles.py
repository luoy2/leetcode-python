'''
There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:


Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.
Example 2:


Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.
 

Constraints:

3 <= s.length <= 105
s consists of '*' and '|' characters.
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plates-between-candles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import *

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pass





from collections import defaultdict
bound_dict = defaultdict(tuple)
s = "*|*||||**|||||||*||*||*||**|*|*||*"
queries = [[2,33],[2,32],[3,31],[0,33],[1,24],[3,20],[7,11],[5,32],[2,31],[5,31],[0,31],[3,28],[4,33],[6,29],[2,30],[2,28],[1,30],[1,33],[4,32],[5,30],[4,23],[0,30],[3,10],[5,28],[0,28],[4,28],[3,33],[0,27]]
# [9, 9, 9, 10, 6, 4, 0, 9, 9, 9, 10, 7, 9, 8, 8, 7, 9, 10, 9, 8, 5, 9, 2, 7, 8, 7, 9, 8]
i = 0
j = 1
cur_left = -1
cur_right = -1
while j < len(s):
    print(i, j, s[i], s[j])
    while s[j] != '|':
        if j == len(s) - 1:
            break
        j += 1
    if s[i] == '|' and s[j] == '|':
        result = (i, j, j-i-1)
    elif s[i] != '|' and s[j] == '|':
        result = (-1, j, 0)
    elif s[i] == '|' and s[j] != '|':
        result = (i, j, 0)
    else:
        result = (-1, j, 0)
    for _ in range(i, j):
        bound_dict[_] = result
    i = j
    j += 1
bound_dict[i] = (bound_dict[i-1][1], i, 0)

# search

result_list = []
for q in queries:
    left_idx, right_idx = q
    total = 0
    while left_idx < right_idx:
        prev_left, next_right, add = bound_dict[left_idx]
        print(prev_left, next_right, add)
        if prev_left >= left_idx:
            if next_right > right_idx:
                break
            total += add
        left_idx = next_right
    result_list.append(total)

print(result_list)



# method2



from collections import defaultdict
bound_dict = defaultdict(tuple)
Input: s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]

# Output: [9,0,0,0,0]
# [9, 9, 9, 10, 6, 4, 0, 9, 9, 9, 10, 7, 9, 8, 8, 7, 9, 10, 9, 8, 5, 9, 2, 7, 8, 7, 9, 8]
i = 0
j = 1
num_list = []
while j < len(s):
    while s[j] != '|':
        if j == len(s) - 1:
            break
        j += 1
    if s[i] == '|' and s[j] == '|':
        result = (i, j, j-i-1)
        if j-i-1:
            num_list.append(result)
    i = j
    j += 1

# search
head_dict = {}
head_num = 0
for i in range(len(s)):
    start, end, _ = num_list[head_num]
    if i > start:
        head_num += 1
    head_dict[i] = head_num
    if head_num == len(num_list):
        break
for i in range(i, len(s)):
    head_dict[i] = -1

# search
tail_dict = {}
if len(num_list):
    first_end = num_list[0][1]
else:
    first_end = len(s)
for i in range(first_end):
    tail_dict[i] = -1


tail_num = 0
for i in range(first_end, len(s)):
    start, end, _ = num_list[tail_num]
    if i >= end:
        tail_num += 1
    tail_dict[i] = tail_num
    if tail_num == len(num_list):
        break
for i in range(i, len(s)):
    tail_dict[i] = tail_num

result_list = []
for q in queries:
    left_idx, right_idx = q
    head = head_dict[left_idx]
    tail = tail_dict[right_idx]
    total = 0
    if head != -1 and tail != -1:
        total += sum([a[2] for a in num_list[head:tail]])
    result_list.append(total)

print(result_list)


## 第三次优化



s = "*|*||||**|||||||*||*||*||**|*|*||*"
queries = [[2,33],[2,32],[3,31],[0,33],[1,24],[3,20],[7,11],[5,32],[2,31],[5,31],[0,31],[3,28],[4,33],[6,29],[2,30],[2,28],[1,30],[1,33],[4,32],[5,30],[4,23],[0,30],[3,10],[5,28],[0,28],[4,28],[3,33],[0,27]]
# [9, 9, 9, 10, 6, 4, 0, 9, 9, 9, 10, 7, 9, 8, 8, 7, 9, 10, 9, 8, 5, 9, 2, 7, 8, 7, 9, 8]
s = "**|**|***|"
queries = [[2,5],[5,9]]


head_dict = {}
tail_dict = {}
prev_h = 0
prev_t = 0
cnt = 0
i = 0
j = 1
num_list = []
while i < len(s) and j < len(s):
    for i in range(i, len(s)):
        if s[i] == '|':
            break
    j = i + 1
    if j == len(s):
        break
    for j in range(j, len(s)):
        if s[j] == '|':
            break
    if s[j] == '|':
        print(i, j)
        if j - i > 1:
            num_list.append(j-i-1)
            for _ in range(prev_h, i+1):
                head_dict[_] = cnt
            for _ in range(prev_t, j):
                tail_dict[_] = cnt
            cnt += 1
            tail_dict[j] = cnt
            prev_h = i+1
            prev_t = j+1
            print(head_dict, tail_dict)
    i = j
for j in range(prev_t, len(s)):
    tail_dict[j] = tail_dict[prev_t - 1]
print(head_dict)
print(tail_dict)

result_list = []
for q in queries:
    left_idx, right_idx = q
    head = head_dict.get(left_idx, -1)
    tail = tail_dict.get(right_idx, -1)
    total = 0
    if head != -1 and tail != -1:
        total += sum(num_list[head:tail])
    result_list.append(total)

print(result_list)


## 第4次优化

from collections import defaultdict
bound_dict = defaultdict(tuple)
s = "*|*||||**|||||||*||*||*||**|*|*||*"
queries = [[2,33],[2,32],[3,31],[0,33],[1,24],[3,20],[7,11],[5,32],[2,31],[5,31],[0,31],[3,28],[4,33],[6,29],[2,30],[2,28],[1,30],[1,33],[4,32],[5,30],[4,23],[0,30],[3,10],[5,28],[0,28],[4,28],[3,33],[0,27]]
# [9, 9, 9, 10, 6, 4, 0, 9, 9, 9, 10, 7, 9, 8, 8, 7, 9, 10, 9, 8, 5, 9, 2, 7, 8, 7, 9, 8]
n = len(s)
preSum, sum = [0] * n, 0
left, l = [0] * n, -1
for i, ch in enumerate(s):
    if ch == '*':
        sum += 1
    else:
        l = i
    preSum[i] = sum
    left[i] = l

right, r = [0] * n, -1
for i in range(n - 1, -1, -1):
    if s[i] == '|':
        r = i
    right[i] = r

ans = [0] * len(queries)
for i, (x, y) in enumerate(queries):
    x, y = right[x], left[y]
    if x >= 0 and y >= 0 and x < y:
        ans[i] = preSum[y] - preSum[x]