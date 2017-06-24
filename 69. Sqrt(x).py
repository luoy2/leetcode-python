# Implement int sqrt(int x).
#
# Compute and return the square root of x.


# My approach:
x = 9.24

def mysqrt(x):
    target = int(x)
    end = int(x)
    start = 0
    z = (end - start)//2
    print(z)
    while z:
        print(z, start, end)
        if z*z == target:
            return (z)
        elif z*z < target:
            start = z
        elif z*z > target:
            end = z
        z = (end - start) // 2
    return (0)


dict = {1:2, 3:4}
dict.get(4, 'busted')