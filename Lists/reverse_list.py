""" Reverse a list. """

# ------------------------------------------
l = [1, 2, 3, 4, 5]
l.reverse()
print('Reversed list Method 1:', l)

# ------------------------------------------
l = [1, 2, 3, 4, 5]
print('Reversed list Method 2:', l[::-1])

# ------------------------------------------
l = [1, 2, 3, 4, 5]
print('Reversed list Method 3:', list(reversed(l)))

# ------------------------------------------
l = [1, 2, 3, 4, 5]
result = []

for n in l:
    result.insert(0,n)
print('Reversed list Method 4:', result)