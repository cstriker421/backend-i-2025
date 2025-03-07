import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_execution_time(func): # Decorator that logs execution time of function

    def wrapper(*args, **kwargs):
        start_time = time.time()                # Records start time
        result = func(*args, **kwargs)          # Calls the function
        end_time = time.time()                  # Records the end time
        execution_time = end_time - start_time  # Calculates the execution time
        
        # Logs the execution time using logging module
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        
        return result  # Returns the result of the function call
    return wrapper

# Example functions provided by ChatGPT
@log_execution_time
def example_function():
    """Simulate a function that takes some time to execute."""
    time.sleep(2)

@log_execution_time
def add_numbers(a, b):
    """A function that adds two numbers."""
    time.sleep(1)
    return a + b

# Example usage
if __name__ == "__main__":
    example_function()
    result = add_numbers(5, 7)
    print(f"Result of add_numbers: {result}")

# Output
"""
    2025-03-07 20:26:18,705 - INFO - Execution time of example_function: 2.0004 seconds
    2025-03-07 20:26:19,709 - INFO - Execution time of add_numbers: 1.0039 seconds
    Result of add_numbers: 12
"""