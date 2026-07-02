""" Reverse a list without using built-in methods. """

l = [1, 2, 3, 4, 5]
result = []

for i in range(len(l)-1,-1,-1):
    result.append(l[i])
print(result)

# ------------------------------------------
l = [1, 2, 3, 4, 5]
i = len(l)-1
result = []

for _ in l:
    result.append(l[i])
    i -= 1
print(result)

# ------------------------------------------
l = [1, 2, 3, 4, 5]
i = 0
j = len(l)-1
while i<j:
    l[i],l[j] = l[j],l[i]
    i += 1
    j -= 1

print(l)
