'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
'''

#my solution
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums)*len(nums[0]):
            return nums
        elif not r or not c:
            return nums
        else:
            nums = [j for i in nums for j in i]
            result = []
            for row in range(r):
                result.append(nums[row*c:(row+1)*c])
            return result
            
            
 # other's solution
 # Solution 1 - NumPy
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
# Solution 2 - Oneliner

def matrixReshape(self, nums, r, c):
    return nums if len(sum(nums, [])) != r * c else map(list, zip(*([iter(sum(nums, []))]*c)))
#A more readable version of that:

def matrixReshape(self, nums, r, c):
    flat = sum(nums, [])
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)
#Solution 3 - itertools

def matrixReshape(self, nums, r, c):
    if r * c != len(nums) * len(nums[0]):
        return nums
    it = itertools.chain(*nums)
    return [list(itertools.islice(it, c)) for _ in xrange(r)]
