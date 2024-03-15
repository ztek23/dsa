def binary_search(x,integer,start,end): # start end integer are index numbers
    mid = start+end//2
    if start <= end:
        if x[mid] == integer:
            return mid
        elif integer > x[mid]:
            return binary_search(x,integer,mid+1,end)
        elif integer < x[mid]:
            return binary_search(x,integer,start,mid-1)
    else:
        return -1
        
print(binary_search([1, 2, 3, 4, 5, 6, 7], 3, 0, 6))



