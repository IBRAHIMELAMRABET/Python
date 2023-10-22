# i = len(L)-1
# while i >= 0:
#     nb = L[i]
#     if L.count(nb) > 1:
#         L.remove(nb)
#     else:
#         i -= 1
# print("Liste après suppression :", L)

L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]
i = len(L) - 1
while i >= 0:
    nb = L[i]
    if L.count(nb) > 1:
        L.pop(i)
    i -= 1
print("Liste après suppression :", L)
