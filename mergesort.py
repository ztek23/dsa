#min, mid, and max are not the lowest or the largest values, they are just index 
def mergeSort(x, min, mid, max):
    start1 = min
    start2 = mid+1
    y = []
    while start1 <= mid and start2 <= max:
        if x[start1] < x[start2]:
            y.append(x[start1])
            start1 = start1+1
        else:
            y.append(x[start2])
            start2 = start2+1
    
    while start1 <= mid:
        y.append(x[start1])
        start1 = start1+1

    while start2 <= max:
        y.append(x[start2])
        start2 = start2+1

    nul = 0
    for i in range(min,max+1):
        x[i] = y[nul]
        nul = nul+1
    print(x)
list = [2, 5, 6, 8, 4, 3]

mergeSort(list, 0, 2, 5)



