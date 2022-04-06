'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


nums = [1,2]
pre_dict = {0: 1}
post_dict = {len(nums)-1: 1}
ans = [0] * len(nums)

def get_pre(i, pre_dict):
    if i not in pre_dict:
        pre_dict[i] = nums[i-1] * get_pre(i-1, pre_dict)
    return pre_dict[i]

def get_post(i, post_dict):
    if i not in post_dict:
        post_dict[i] = nums[i+1] * get_post(i+1, post_dict)
    return post_dict[i]

for i, n in enumerate(nums):
    ans[i] = get_pre(i, pre_dict) * get_post(i, post_dict)
print(ans)


# 解法2
nums = [1,2, 3]
ans = [1]
p = 1
q = 1

for i, n in enumerate(nums[:-1]):
    p *= n
    ans.append(p)
print(ans)
# [1, 1, 2]
这是nums每个左边部分的乘积
1: 左边为1（因为没有）
2: 左边为1
3: 左边为1*2

现在要算每个数右边的乘积
3：右边为1（因为没有）
2：右边为3*1
1：右边为3*2*1

为了节约空间，所以现在要倒过来计算，得出结论：
3： 2（左）*1（右）
2： 1（左）* 3*1（右，上一步算好）
1： 1（左）* 2*3（右，上一步算好）

q = 1
for i in range(len(nums)-1, -1, -1):
    ans[i] *= q
    q *= nums[i]
print(ans)