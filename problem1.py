#1. Sum of all items in a list
a = [1, 2, 3, 4,65,74,97,8,9,10,11,12,13,14,15,16,17,18,19,20]
count = 0
for i in range(0, len(a)):
    count += a[i]
print(count)