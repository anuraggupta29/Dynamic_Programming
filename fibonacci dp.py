n = int(input())

fib_map = [0, 1]

while len(fib_map) < n + 1:
    fib_map.append(0)

def fibonacci(n):
    global fib_map

    if n <= 1:
        return n

    else:
        if fib_map[n-1] == 0:
            fib_map[n-1] = fibonacci(n-1)

        if fib_map[n-2] == 0:
            fib_map[n-2] = fibonacci(n-2)

    fib_map[n] = fib_map[n-1] + fib_map[n-2]
    return fib_map[n]

print(fibonacci(n))
