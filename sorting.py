x = [7, 4, 1, 2, 3, 6, 9, 8]
x.sort(reverse=True)
print(x)

y = [7, 5, 3, 1, 9, 8]

#bubble sort
for i in range(6):
    for j in range(i,6):
        if y[i] < y[j]:
            y[i], y[j] = y[j], y[i]

print(y)
