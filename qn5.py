from functools import reduce

def lcm(*values):
    values = [value for value in values]
    if values:
        n  = max(values)
        m = n
        values.remove(n)
        while any( n % value for value in values ):
            n +=m
        return n
    return 0

k=reduce(lcm, range(1,21))
print(k)