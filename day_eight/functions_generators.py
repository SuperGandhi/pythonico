
def pares():
    arr = []
    for num in range(1,1000):    
        if num % 2 == 0:
            arr.append(num)
    yield arr


result_generator = pares()
result = next(result_generator)
print(result)