import time
from contextlib import contextmanager

@contextmanager
def timer():

    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")

# Example usage
if __name__ == "__main__":
    with timer():
        total = 0
        for i in range(1, 1000000):
            total += i
        print(f"Sum is: {total}")

# Output
"""
    Sum is: 499999500000
    Execution time: 0.13372468399938953 seconds
"""