target = 0
nums = [1, 0, -1, 0, -2, 2]

# Version 1: 把所有的2个数相加的和放进dictionary, 然后再loop through, 看是否可以找到第三个
sum_dict = {}
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        try:
            sum_dict[nums[i] + nums[j]].append([i, j])
        except:
            sum_dict[nums[i] + nums[j]] = [[i, j]]
solution_set = []
# print(sum_dict)


for k in range(len(nums)):
    for v in range(k+1, len(nums)):
        if target - nums[k] - nums[v] in sum_dict.keys():
            for subset in sum_dict[target - nums[k] - nums[v]]:
                if subset[0] > v: #从头开始loop, 只需知道剩下的两个数的index比v大就好
                    temp_set = sorted([nums[k], nums[v], nums[subset[0]], nums[subset[1]]])
                    if temp_set not in solution_set:
                        solution_set.append(temp_set)


# print(solution_set)
#
#
# print(solution_set)
# dictionnary: {0: [[0, 2], [1, 3], [4, 5]], 1: [[0, 1], [0, 3], [2, 5]], 2: [[1, 5], [3, 5]], 3: [[0, 5]], -1: [[0, 4], [1, 2], [2, 3]], -3: [[2, 4]], -2: [[1, 4], [3, 4]]}
# [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
# 运行超时

# version 2:
# change if target - nums[k] - nums[v] in sum_dict.keys() into if target - nums[k] - nums[v] in sum_dict,
                        # dramatically reduce runtime

x = {2:3, 3:4, 4:5, 5:6}
def f1(z):
    if z in x:
        x[z] = 0

def f2(z):
    if z in x.keys():
        x[z] = 0

# In[13]: %timeit f1(2)
# 10000000 loops, best of 3: 144 ns per loop
# In[14]: %timeit f2(2)
# The slowest run took 10.60 times longer than the fastest. This could mean that an intermediate result is being cached.
# 1000000 loops, best of 3: 227 ns per loop
