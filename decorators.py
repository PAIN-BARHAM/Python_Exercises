import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do ..
        result = func(*args, **kwargs)
        print('End')
        # Do ..
        return result
    return wrapper


@start_end_decorator
def add5(x):
    return x + 5


# print_name = start_end_decorator(print_name)

print(add5(2))

print(add5.__name__)
print(help(add5))
