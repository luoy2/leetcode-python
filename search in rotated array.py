class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            print(left, right, mid)
            if nums[mid] == target:
                return (mid)
            elif nums[left] == target:
                return (left)
            elif nums[right] == target:
                return (right)

            if nums[mid] > nums[left]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                elif nums[left] < nums[mid] < target:
                    left = mid + 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target < nums[left]:
                    left = mid + 1
                elif nums[mid] < nums[left] < target:
                    right = mid -1
                else:
                    right = mid - 1

            else:
                return (-1)
        return (-1)


if __name__ == "__main__":
    print(Solution().search([5,1,2,3,4], 1))
