'''
def play(n):
    for i in range(n,0,-1):
        print( i, end= " ")
    

    for i in range( 1, n+1):
        print( i, end= " ")


n = int(input("Enter a number: "))
play(n)
'''
#Performing same activity using recursion
def play2(n):
    #case from where backtracking starts taking place
    #Stack overflow happens if this case is absent                                 
    if n <1: #base case (making recursive function stop after a while)
        return
    else:
        print(n, end= " ")
        play2( n-1 )
        print(n, end = " ")
        return
    
play2( 5)