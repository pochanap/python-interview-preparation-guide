''' find even and odd numbers '''
l = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for num in l:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even: ",even)
print("Odd: ",odd)