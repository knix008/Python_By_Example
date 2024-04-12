import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Finished in {:.3f} secs".format(end - start))
        return result

    return wrapper


@timer
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000)
# Prints Finished in 0.005 secs
countdown(1000000)
# Prints Finished in 0.178 secs
