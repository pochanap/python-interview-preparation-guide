''' Flatten a list of Lists using recusion '''

def flatten_list(l):
    result = []
    for item in l:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

l = [[1, 2], 3, [4, 5], [6, 7,8],9,10]
print(flatten_list(l))

# ------------------------------------------

l = [[1, 2, 3], [4, 5], [6, 7]]
result = []

for sub in l:
    for item in sub:
        result.append(item)
print(result)
