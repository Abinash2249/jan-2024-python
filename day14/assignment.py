# WAP to create a decorator function which calculates the total time to execute the following functions



@execution_time
def func():
    for i in range(1000000000):
        continue
    print(("Loop complete !!"))

func()


# import time
# start = time.time()
# a = 1
# b = 2
# print(a+b)
# end = time.time()
# total_time = end - start
# print(total_time)

