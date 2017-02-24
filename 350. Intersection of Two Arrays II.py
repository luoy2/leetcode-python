# Total Accepted: 53040
# Total Submissions: 121093
# Difficulty: Easy
# Contributors: Admin
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
#


# 1. Sorted:

nums1 = [1, 2, 2, 1]
nums2 = [1, 1, 3]

nums1.sort()
nums2.sort()

ans = []
p1, p2 = 0, 0
if nums1 and nums2:
    if nums1[0] > nums2[0]:
        nums1, nums2 = nums2, nums1
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            ans.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
print(ans)


# 2. Hash
dict = {i:nums1.count(i) for i in set(nums1)}
ans = []
for elem in nums2:
    try:
        if dict[elem] > 0:
            dict[elem] -= 1
            ans.append(elem)
    except KeyError:
        next
print(ans)


# 3. Other's ans
