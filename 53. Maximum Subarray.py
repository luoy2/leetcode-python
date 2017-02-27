# 53. Maximum Subarray Add to List
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


nums = [-2,1,-3,4,-1,2,1,-5,4]

ans = 0
def rec_solv(pos, ans):
    if pos == len(nums) - 1:
        x = nums[pos]
    else:
        x = max(nums[pos]+rec_solv(pos+1, ans), nums[pos])
        ans = max(ans, x)
    print(ans)
    return(x)

print(rec_solv(0, 0))