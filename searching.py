a = []

#first method
'''
for i in range(10):
    n = int(input("Enter a number: "))
    a.append(n)
'''

#second method
'''
info = list (map ( int, input("Enter the numbers: ").split(",") ))
print(info)

n = int(input("Enter the number you want to search in the list: "))

if n in info:
    for i in range(len(info)):
        if n == info[i]:
            print("{} found at {}".format(n, i+1))
'''

#binary search
#information must always be arranged! (increasing or decreasing order)

info = list (map ( int, input("Enter the numbers: ").split() ))
n = int(input("Enter the value you want to search: "))

start = 0
end = len(info) - 1
flag = False
while start <= end:
    mid = start+end//2
    if info[mid] == n:
        print("{} found at {}".format(n, mid+1))
        flag = True
        break
    elif n > info[mid]:
        start = mid+1
    elif n < info[mid]:
        end = mid-1

if flag == False:
    print("Value not present")
