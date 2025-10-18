def fib(inp):
    if inp == 0:
        return 0
    if inp == 1:
        return 1
    return fib(inp - 1) + fib(inp - 2)

def powerOf(inp, power):
    if power == 0:
        return 1
    return powerOf(inp, (power - 1)) * inp

print(powerOf(3, 2))