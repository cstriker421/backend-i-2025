import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Authentication decorator
def authenticate(username):
    valid_users = ["admin", "manager", "user123"]

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if username not in valid_users:
                logging.warning(f"Authentication failed for user: {username}")
                raise PermissionError("Authentication failed: Invalid username")
            logging.info(f"User {username} authenticated successfully.")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Caching decorator
def cache_results(func): # Decorator logs when results are cached or computed. Logs cache hits and misses

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        cache_info = func.cache_info()  # Calls cache_info() on the function wrapped by lru_cache
        if cache_info.hits > 0:
            logging.info(f"Using cached result for {func.__name__} with arguments {args}")
        else:
            logging.info(f"Computing result for {func.__name__} with arguments {args}")
        
        return func(*args, **kwargs)
    
    return wrapper


# Applies lru_cache to the factorial function
@authenticate("manager")  # Simulates a valid user (manager)
@cache_results  # Logs cache usage (apply after caching)
@functools.lru_cache(maxsize=None)  # Caches results of the factorial computation (apply first)
def factorial(n):
    """Computes the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    time.sleep(0.5)
    return n * factorial(n - 1)


# Example of a function that requires authentication
@authenticate("admin")  # Simulates a valid user (admin)
def sensitive_function():
    return "Sensitive data accessed"


# Demonstrative usage
if __name__ == "__main__":

    print(factorial(5))  # Computation will happen
    print(factorial(6))  # Cached result will be used
    
    try: # Attempts to call the function with an invalid user (authentication failure)
        @authenticate("invalid_user")
        def sensitive_function_invalid():
            return "Sensitive data accessed"
        print(sensitive_function_invalid())
    except PermissionError as e:
        print(f"Error: {e}")
