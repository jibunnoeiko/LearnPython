import time

# Without Helper Function
def do_things():
    start_time = time.perf_counter()
    for i in range(10):
        y = i ** 100
        print(time.perf_counter() - start_time, "seconds elapsed")
    x = 10**2
    print(time.perf_counter() - start_time, "seconds elapsed")
    return f'{x}\n'

print(do_things())


# With Helper Function
import time

def print_time_elapsed(start_time):
    print(time.perf_counter() - start_time, 'seconds elapsed')
def do_things():
    start_time = time.perf_counter()
    for i in range(10):
        y = i ** 100
        print_time_elapsed(start_time)
    x = 10 ** 2
    print_time_elapsed(start_time)
    return x

print(do_things())
