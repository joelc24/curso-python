mi_set = set((1,2,3,4,5,(6,7,8)))

print(type(mi_set))
print(mi_set)

otro_set = {9,10,11}
otro_set.add(12)
otro_set.discard(12)
print(otro_set)
print(7 in mi_set)
print(mi_set.union(otro_set))