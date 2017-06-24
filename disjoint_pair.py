A = [1, 12, 42, 70, 36, -4, 43, 15]
B = [5, 15, 44, 72, 36, 2, 69, 24]

my_d = {}
for pos in range(len(A)):
    my_d[A[pos]] = B[pos]

import collections

d = {1: 3, 4: 2, 2: 5}
od = collections.OrderedDict(sorted(my_d.items()))

ans = 1
keys = list(od)
if len(od) >= 2:
    for pos, key in enumerate(keys):
        if pos < len(od) - 1:
            if keys[pos+1] > od[key]:
                ans += 1
print(ans)
