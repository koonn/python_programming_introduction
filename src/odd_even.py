def min_odd(x, y, z):
    if x%2 != 0 and y%2 != 0 and z%2 != 0:
        return min(x, y, z)
    elif x%2 != 0 and y%2 != 0 and z%2 == 0:
        return min(x, y)
    elif x%2 != 0 and y%2 == 0 and z%2 != 0:
        return min(x, z)
    elif x%2 == 0 and y%2 != 0 and z%2 != 0:
        return min(y, z)
    elif x%2 != 0 and y%2 == 0 and z%2 == 0:
        return x
    elif x%2 == 0 and y%2 != 0 and z%2 == 0:
        return y
    elif x%2 == 0 and y%2 == 0 and z%2 != 0:
        return z
    else:
        return min(x, y, z)
