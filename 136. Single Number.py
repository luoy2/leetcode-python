# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# My solution:
nums = [1,2,3,2,3]
result = list(set(nums))
my_dict = {}
for i in nums:
    if i in my_dict:
        my_dict[i] += 1
        result.remove(i)
    else:
        my_dict[i] = 1

print(result)


#  Best Solution so far:
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)