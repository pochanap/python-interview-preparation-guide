''' Merge two list '''

l1 = [1,2,3]
l2 = [3,4,5]

l1.extend(l2)
print(l1)

''' Common elements of two list '''
l1 = [1,2,3,5]
l2 = [3,4,5]
seen = set()
for num in l1:
    if num in l2:
        seen.add(num)
print(seen)


''' Unique elements of two list '''
l1 = [1,2,3,5]
l2 = [3,4,5]
result = []
for num in l1:
    if num not in l2:
        result.append(num)

for num in l2:
    if num not in l1:
        result.append(num)
print(result)