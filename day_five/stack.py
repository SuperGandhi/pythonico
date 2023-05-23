"""
    Implementation to stack with procedimental programming
    
"""
stack = []


def push(val):
    stack.append(val)


def pop(val):
    val = stack[-1]
    del stack[-1]
    return val 


push(3)
push(4)
push(10)

print(pop())
print(pop())
print(pop())


"""
    Implementation to stack with POO

"""



class Stack:
    pass

    