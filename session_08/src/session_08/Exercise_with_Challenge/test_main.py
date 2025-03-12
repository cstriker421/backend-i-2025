import pytest
from typer.testing import CliRunner
from main import app

runner = CliRunner()

def test_add(): # Tests the 'add' command by simulating user input
    
    result = runner.invoke(app, ["add"], input="2\n3\n")
    assert result.exit_code == 0
    assert "The sum of 2.0 and 3.0 is 5" in result.output

def test_subtract(): # Tests the 'subtract' command by simulating user input
    
    result = runner.invoke(app, ["subtract"], input="10\n5\n")
    assert result.exit_code == 0
    assert "The difference between 10.0 and 5.0 is 5" in result.output

def test_square(): # Tests the 'square' command by simulating user input
    
    result = runner.invoke(app, ["square"], input="-4\n")
    assert result.exit_code == 0
    assert "The square of -4.0 is 16" in result.output

def test_invalid_command(): # Tests the case where the user enters an invalid command (e.g., a non-existent command)
    
    result = runner.invoke(app, ["multiply", "4", "2"])
    assert result.exit_code != 0
    assert "No such command 'multiply'" in result.output
