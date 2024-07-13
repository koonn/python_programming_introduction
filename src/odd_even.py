def max_odd_or_min_even(x, y, z):
    answer = min(x, y, z)
    if x%2 != 0:
        answer = x
    if y%2 != 0 and y > answer:
        answer = y
    if z%2 != 0 and z > answer:
        answer = z
    return answer

# def max_odd_or_min_even(x, y, z):
#     if x%2 != 0 and y%2 != 0 and z%2 != 0:
#         return max(x, y, z)
#     elif x%2 != 0 and y%2 != 0 and z%2 == 0:
#         return max(x, y)
#     elif x%2 != 0 and y%2 == 0 and z%2 != 0:
#         return max(x, z)
#     elif x%2 == 0 and y%2 != 0 and z%2 != 0:
#         return max(y, z)
#     elif x%2 != 0 and y%2 == 0 and z%2 == 0:
#         return x
#     elif x%2 == 0 and y%2 != 0 and z%2 == 0:
#         return y
#     elif x%2 == 0 and y%2 == 0 and z%2 != 0:
#         return z
#     else:
#         return max(x, y, z)