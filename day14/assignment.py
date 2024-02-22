# WAP to create a decorator function which calculates the total time to execute the following functions



def execution_time(funct):
    def inner_function(*args, **kwargs):
        import time
        start = time.time()
        result = funct(*args, **kwargs)
        end = time.time()
        elapsed_time = end - start
        print(f"The total elapsed time to execute the function was: {elapsed_time}")
        return result
    return inner_function



@execution_time
def func():
    for i in range(1000000000):
        continue
    print(("Loop complete !!"))


func()


import time
start = time.time()
a = 1
b = 2
print(a+b)
end = time.time()
total_time = end - start
print(total_time)

