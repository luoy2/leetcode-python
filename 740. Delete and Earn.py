'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''

nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]
from collections import Counter
c = Counter(nums)

def get_point(delete_idx, nums, sum_):
    num_to_delete = nums[delete_idx]
    leftovers = []
    for i, n in enumerate(nums):
        if i == delete_idx:
            continue
        if n not in [num_to_delete+1, num_to_delete-1]:
            leftovers.append(n)
    sum_ += num_to_delete
    if not leftovers:
        return sum_
    else:
        scores = []
        for idx in range(len(leftovers)):
            scores.append(get_point(idx, leftovers, sum_))
        return max(scores)


scores = [0]
for idx in range(len(nums)):
    scores.append(get_point(idx, nums, 0))
max(scores)




def get_point(num_to_delete, nums, sum_):
    candidates = {}
    leftovers = []
    for n in nums:
        if n == num_to_delete:
            sum_ += n
        elif n not in [num_to_delete+1, num_to_delete-1]:
            leftovers.append(n)
            candidates[n] = 0
    if not candidates:
        return sum_
    else:
        scores = []
        for cand in candidates:
            scores.append(get_point(cand, leftovers, sum_))
        return max(scores)


scores = [0]
for s in set(nums):
    scores.append(get_point(s, nums, 0))
max(scores)






# 思路为从后面往前走，当前数的收益 =  max(删除当前数的收益（n*count(n))+当前数+2的收益， 保留当前数（0） + 当前数+1的收益）
nums = [2,4,5,5,6,6,6]
from collections import Counter

c = Counter(nums)
sorted_nums = [i for i in sorted(c.keys())]
# if len(c) < 2:
#     return sorted_nums[0] * c[sorted_nums[0]]
gains = {}
gains = [0] * len(sorted_nums)
gains[-1] = c[sorted_nums[-1]] * sorted_nums[-1]
if sorted_nums[-2] == sorted_nums[-1] - 1:
    gains[-2] = max(sorted_nums[-2] * c[sorted_nums[-2]], gains[-1])
else:
    gains[-2] = sorted_nums[-2] * c[sorted_nums[-2]] + gains[-1]

for i in range(len(sorted_nums)-3, -1, -1):
    key = sorted_nums[i]
    print(i, key)
    if key + 1 not in c:
        gains[i] = gains[i+1] + key*c[key]
    else:
        gains[i] = max(gains[i+1], key*c[key] + gains[i+2])

print(gains[0])


# 优化空间

nums = [1,6,3,3,8,4,8,10,1,3]
from collections import Counter


c = Counter(nums)
sorted_nums = [i for i in sorted(c.keys())]
# if len(c) < 2:
#     return sorted_nums[0] * c[sorted_nums[0]]
curr = c[sorted_nums[-1]] * sorted_nums[-1]

if sorted_nums[-2] == sorted_nums[-1] - 1:
    prev = max(sorted_nums[-2] * c[sorted_nums[-2]], curr)
else:
    prev = sorted_nums[-2] * c[sorted_nums[-2]] + curr


for i in range(len(sorted_nums)-3, -1, -1):
    key = sorted_nums[i]
    print(i, key)
    print(prev, curr, end='')
    if key + 1 not in c:
        print("直接")
        prev, curr = prev + key*c[key], prev
    else:
        print("决策")
        prev, curr = max(prev, key*c[key]+curr), prev
    print("---->", end='')
    print(prev, curr)
print(prev)