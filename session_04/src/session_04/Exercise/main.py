class EvenIterator:
    def __init__(self, numbers): # Iterator to filter even numbers(list)

        self.numbers = numbers
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self): # Gets next even number(int) from list

        while self.index < len(self.numbers):
            number = self.numbers[self.index]
            self.index += 1
            if number % 2 == 0:
                return number
        raise StopIteration

def fibonacci_generator(limit): # Fibonacci Number generator that goes up to a limit(int)

    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_iterator = EvenIterator(numbers)

    print("Even numbers from the list:")
    for even_number in even_iterator:
        print(even_number)

    limit = 10
    print(f"\nFirst {limit} Fibonacci numbers:")
    for fib_number in fibonacci_generator(limit):
        print(fib_number)

    # Output
    """
        Even numbers from the list:
        2
        4
        6
        8
        10

        First 10 Fibonacci numbers:
        0
        1
        1
        2
        3
        5
        8
        13
        21
        34
    """