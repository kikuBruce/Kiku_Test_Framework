import time
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print(time.ctime())

print(now.__name__)