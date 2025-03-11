import time

class Timer:
    def __enter__(self):

        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.end_time = time.perf_counter()
        execution_time = self.end_time - self.start_time
        print(f"Execution time: {execution_time} seconds")

# Example usage
if __name__ == "__main__":
    with Timer():
        total = 0
        for i in range(1, 1000000):
            total += i
        print(f"Sum is: {total}")

# Output
"""
    Sum is: 499999500000
    Execution time: 0.13327197500075272 seconds
"""