import subprocess
import socket
import time
import pytest
import sys

# Test case to ensure the server starts up before tests
@pytest.fixture(scope="session")
def server():
    # Start the server
    server_process = subprocess.Popen(
        ["poetry", "run","server"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    # Waits for the server to start, checking the process output
    retries = 10
    for _ in range(retries):
        try:
            with socket.create_connection(('127.0.0.1', 8080), timeout=5):
                break
        except (ConnectionRefusedError, OSError) as e:
            time.sleep(1)
    else:
        pytest.fail("Server did not start within the expected time.")
    yield server_process

    # Terminates the server after tests
    server_process.terminate()
    try:
        server_process.wait(timeout=5)  # Waits for the server to shut down gracefully
    except subprocess.TimeoutExpired:
        server_process.kill()  # Force kills it if it takes too long

def test_home_page(server):
    # Prepares a mock client connection (this will simulate the request-response cycle)
    with socket.create_connection(("127.0.0.1",8080),timeout=5) as client_socket:
        client_socket.sendall(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
        
        response = client_socket.recv(1024).decode('utf-8')
        
        # Check if the response contains the correct status code
        assert "HTTP/1.1 200 OK" in response
        assert "<h1>Welcome to the Home Page!</h1>" in response
        assert "Content-Length:" in response
        
        # Get the content length from the response header
        content_length = int(response.split("Content-Length: ")[1].split("\r\n")[0])
        assert content_length == len("<html><body><h1>Welcome to the Home Page!</h1></body></html>")

def test_about_page(server):
    # Prepare a mock client connection (this will simulate the request-response cycle)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 8080))
        client_socket.sendall(b"GET /about HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
        
        response = client_socket.recv(1024).decode('utf-8')
        
        # Check if the response contains the correct status code
        assert "HTTP/1.1 200 OK" in response
        assert "<h1>About Us</h1>" in response
        assert "We are a simple HTTP server." in response
        assert "Content-Length:" in response
        
        # Get the content length from the response header
        content_length = int(response.split("Content-Length: ")[1].split("\r\n")[0])
        assert content_length == len("<html><body><h1>About Us</h1><p>We are a simple HTTP server. Ignore us!</p></body></html>")

def test_404_error(server):
    # Prepares a mock client connection (this will simulate the request-response cycle)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 8080))
        client_socket.sendall(b"GET /nonexistent HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
        
        response = client_socket.recv(1024).decode('utf-8')
        
        # Checks if the response contains the correct status code
        assert "HTTP/1.1 404 Not Found" in response
        assert "<h1>404 Error</h1>" in response
        assert "Nothing here but grues!" in response
        assert "Content-Length:" in response
        
        # Gets the content length from the response header
        content_length = int(response.split("Content-Length: ")[1].split("\r\n")[0])
        assert content_length == len("<html><body><h1>404 Error</h1><p>Nothing here but grues!</p></body></html>")
