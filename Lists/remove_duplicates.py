'''remove duplicates'''
l = [2, 4, 1, 4, 2, 3,1,5]
result = []

for num in l:
    if num not in result:
        result.append(num)

print(result)
