import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function execution time {func.__name__}: {execution_time} seconds.")
        return result
    return wrapper

# Тестовый вызов функции


@measure_time
def calculate_sum(n):
    sum_result = 0
    for i in range(1, n+1):
        sum_result += i
    return sum_result


result = calculate_sum(1000000)
print(f"Result: {result}")
