def sum_number(n):
    if n == 0:
        return 0
    return n + sum_number(n - 1)


# a = sum_number(5)
# print(a)
print(sum_number(5))