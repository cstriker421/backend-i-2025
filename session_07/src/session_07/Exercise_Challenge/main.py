import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@contextmanager
def exception_suppressor():

    try:
        yield
    except Exception as e: # Logs exception details
        logging.error(f"An exception occurred: {type(e).__name__} - {e}")
        # Suppresses the exception and allows the program to continue
        pass

# Example usage
if __name__ == "__main__":
    with exception_suppressor():
        # Raises a ZeroDivisionError, but catches it and suppresses it
        result = 1 / 0
        print("This will not print if the exception isn't handled.")
    
    print("The program continues running after the exception.")

# Output
"""
    2025-03-11 20:03:03,054 - ERROR - An exception occurred: ZeroDivisionError - division by zero
    The program continues running after the exception.
"""