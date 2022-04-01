'''

Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

 

Example 1:

Input: arr = [3,1,3,6]
Output: false
Example 2:

Input: arr = [2,1,2,6]
Output: false
Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
 

Constraints:

2 <= arr.length <= 3 * 104
arr.length is even.
-105 <= arr[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

arr = [4,-2,2,-4]
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        num_map = collections.Counter(arr)
        for num in sorted(num_map, key=abs):
            if num_map[num] > num_map[2 * num]:
                return False
            num_map[2 * num] -= num_map[num]
        return True
