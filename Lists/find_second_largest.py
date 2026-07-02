'''Second large number'''

def second_large(l):
    largest = second = float('-inf')
    for num in l:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

l = [2, 6, 11, 9, 4, 5, 3,10]
print(second_large(l))