def dead(m, n):
    r = [1] + [0] * (n - 1)
    for i in range(2, m + 1):
        r = [sum(r[1:])] + r[:-1]
    return sum(r)

print(dead(97, 20))