n = int(input("Please enter a number(will be converted to fibonacci): "))

def Fibonacci(n):
    #check if input is 0
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
print(Fibonacci(n))