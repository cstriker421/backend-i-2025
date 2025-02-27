import logging

# Sets up logging configuration
logging.basicConfig(filename='calculator.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_operation(operation: str, result: float):
    logging.info(f"{operation}: {result}")

def add(a, b):
    result = a + b
    log_operation(f"The sum of {a} and {b}", result)
    return result

def subtract(a, b):
    result = a - b
    log_operation(f"The difference of {a} and {b}", result)
    return result

def multiply(a, b):
    result = a * b
    log_operation(f"The product of {a} and {b}", result)
    return result

def divide(a, b):
    if b == 0:
        log_operation(f"Attempted division by zero with {a} and {b}", "Error")
        return "Error: Division by zero"
    result = a / b
    log_operation(f"The quotient of {a} and {b}", result)
    return result

# Example usage
if __name__ == "__main__":
    a = 5
    b = 10
    
    # Performs operations and logs them
    print("The sum of", a, "and", b, "is", add(a, b))               # The sum of 5 and 10 is 15
    print("The difference of", a, "and", b, "is", subtract(a, b))   # The difference of 5 and 10 is -5
    print("The product of", a, "and", b, "is", multiply(a, b))      # The product of 5 and 10 is 50
    print("The quotient of", a, "and", b, "is", divide(a, b))       # The quotient of 5 and 10 is 0.5