''' largest num '''

def largest_number(l):
    large = l[0]
    for n in l:
        if n > large:
            large = n
    return large

l = eval(input("enter elements: "))
print(largest_number(l))