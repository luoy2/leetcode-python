


##我的
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        start_index = 0
        for element in nums:
            my_dict[start_index] = element
            start_index += 1
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        break_val = True
        while break_val:
            num1 = sorted_nums[i]
            num2 = sorted_nums[j]
            attempt_sum = sorted_nums[i] + sorted_nums[j]
            if attempt_sum < target:
                i = i + 1
            elif attempt_sum > target:
                j = j - 1
            else:
                break_val = False
        return_list = []
        for position in range(0, len(nums)):
            if my_dict[position] == num1 or my_dict[position] == num2:
                return_list.append(position)

        return (return_list)

#答案
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []



if __name__ == '__main__':
    print (Solution().twoSum((0, 2, 3, 0), 0))