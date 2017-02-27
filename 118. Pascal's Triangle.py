# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return ([[]])
        elif numRows == 1:
            return ([[1]])
        elif numRows == 2:
            return ([[1], [1, 1]])
        else:
            ans = [[1], [1, 1]]
            for i in range(2, numRows):
                temp_array = [1]
                for j in range(i-1):
                    temp_array.append(ans[i - 1][j] + ans[i - 1][j + 1])
                temp_array.append(1)
                ans.append(temp_array)

        return (ans)


print(Solution().generate(5))