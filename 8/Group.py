import time
from functools import wraps

# декоратор таймерів обгортає орг. ф-ї викоричтовуючі декоратор @wraps(func)

def timer(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f"Время выполнения - {time_end - time_start}")
        return result

    return decorated_function


@timer
def multiply(a, b):
    result = a * b
    print(f"Результат умножения: {result}")
    return result


@timer
def add(a, b):
    result = a + b
    print(f"Результат сложения: {result}")
    return result


if __name__ == "__main__":
    multiply(2, 2)

