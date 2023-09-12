def factorialize(n):
    if n < 0:
        raise ValueError("This number should be uppper or equal to 0")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorialize(n - 1)


# a = 10
# print(factorialize(a))
       