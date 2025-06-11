#3.Find the largest number in a list
a = [5,9,1,7]
count = 0
for i in range(0, len(a)):
    if a[i] > count:
        count = a[i]
    print(count)
