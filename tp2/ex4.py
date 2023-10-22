L = {1, -30, 0, -2, 500, 4, 2, 100}

left = []
right = []

for n in L:
    if n < 0:
        left.append(n)
    else:
        right.append(n)

M = left + right
print(M)