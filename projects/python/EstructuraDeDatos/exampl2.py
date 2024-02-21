def example_algo(n):
    total = 0
    for i in range(n): 
        for j in range(n):
            total += i * j
    for k in range(n):
        if k % 2 == 0:total += k
    return total