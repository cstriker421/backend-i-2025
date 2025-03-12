import logging
import typer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = typer.Typer()

def format_number(number: float):
    """
    Helper function to return the number without decimal point if it is a whole number.
    """
    if number.is_integer():
        return int(number)
    return number

@app.command()
def add():
    """
    Adds two numbers and prints the result.
    The user will be prompted to input the numbers interactively, including negatives.
    """
    a = float(typer.prompt("Enter the first number"))
    b = float(typer.prompt("Enter the second number"))

    logging.info(f"Adding {a} and {b}")
    result = a + b
    result = format_number(result)
    logging.info(f"Result: {result}")
    print(f"The sum of {a} and {b} is {result}")

@app.command()
def subtract():
    """
    Subtracts one number from another and prints the result.
    The user will be prompted to input the numbers interactively, including negatives.
    """
    a = float(typer.prompt("Enter the first number"))
    b = float(typer.prompt("Enter the second number"))

    logging.info(f"Subtracting {b} from {a}")
    result = a - b
    result = format_number(result)
    logging.info(f"Result: {result}")
    print(f"The difference between {a} and {b} is {result}")

@app.command()
def square():
    """
    Squares the given number and prints the result.
    The user will be prompted to input the number interactively, including negatives.
    """
    number = float(typer.prompt("Enter the number"))

    logging.info(f"Squaring {number}")
    result = number ** 2
    result = format_number(result)
    logging.info(f"Result: {result}")
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    app()
