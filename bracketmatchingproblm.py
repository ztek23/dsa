openlist = ["[","{","("]
closelist = ["]","}",")"]

def validator(inp):
    stack = []
    for x in inp:
        if x in openlist:
            stack.append(x)
        elif x in closelist:
            p = closelist.index(x)
            print(p)
            if len(stack) > 0 and openlist[p] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "unbalanced"
    if len(stack) == 0:
        return "balanced"
    else:
        return "unbalanced"
    

user = str(input("Please enter a value with brackets: "))

print(validator(user))
    

