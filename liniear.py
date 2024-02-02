marks = [89,81,85,84,91,94,97,99,98,100]

n = int(input("What mark do you want to search in the marks list? :"))

f = True

for i in range(len(marks)):
    if marks[i]==n:
        f = True
# if the index number is 0, then the position is 1
    print(" Found it at- ",(i+1) )
    
    
if not(f):
    print("Not found")