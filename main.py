def fib(inp):
    if inp == 0:
        return 0
    if inp == 1:
        return 1
    return fib(inp - 1) + fib(inp - 2)

print(fib(4))