# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]


#My Approach:

nums = [4,3,2,7,8,2,3,1]
for i, num in enumerate(nums):

    if i + 1 != num:
        while True:
            nums[i], nums[num - 1] = nums[num - 1], nums[i]
            num = nums[i]
            if num == i + 1:
                break
            elif num == nums[num - 1]:
                nums[i] = 0
                break
            elif num == 0:
                break
print([i+1 for i in range(len(nums)) if nums[i] == 0])

# Other's Approach
# For each number i in nums,
# we mark the number that i points as negative.
# Then we filter the list, get all the indexes
# who points to a positive number.
# Since those indexes are not visited.
# Fantanstic!

nums = [4,3,2,7,8,2,3,1]
for i in range(len(nums)):
    print(nums)
    index = abs(nums[i]) - 1
    nums[index] = - abs(nums[index])
    print(nums)
    print()

print ([i + 1 for i in range(len(nums)) if nums[i] > 0])


