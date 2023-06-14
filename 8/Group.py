import time


def timer(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print(f'Время выполнения - {time_end - time_start}')

    return wrapper


def multiply_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат умножения: {result}")
        return result

    return wrapper


def add_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат сложения: {result}")
        return result

    return wrapper


@timer
@multiply_decorator
def multiply(a, b):
    return a * b


@timer
@add_decorator
def add(a, b):
    return a + b


if __name__ == "__main__":
    multiply(2, 2)
