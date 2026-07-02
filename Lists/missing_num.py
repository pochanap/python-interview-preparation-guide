''' find missing number from sequence '''
l = [1,2,3,5]

for i in range(1,len(l)+2):
    if i not in l:
        print(i)
        break
    
# ------------------------------------------

l = [1,2,3,5]

for i in range(len(l)-1):
    if l[i+1] - l[i] != 1:
        print(l[i]+1)
        break