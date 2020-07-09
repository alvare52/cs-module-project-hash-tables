# Your code here

cache = {}
def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z
    if x not in cache:
        cache[x] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    return cache[x]
    # exps(x, y, z) =
    #  if x <= 0: y + z
    #  if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

# Fibonacci 

    # cache = {}
    # def fib(n):
    #     if n <= 1:
    #         return n


    #     # if n not in cache:
    #         # cache[n] = fib(n-1) + fib(n-2)

    #     # or just this
    #     if n in cache:
    #         return cache[n]
    #     else:
    #         cache[n] = fib(n - 1) + fib(n - 2)
    #     #    
        
    #     return cache[n]

    # print(fib(3))
    # print(fib(5))
    # print(fib(6))
    # print(fib(7))
    # print(fib(50))



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
