import socket
import pytest

# Note, these tests only work if you run the server in another terminal

def test_home_page():
    # Prepares a mock client connection (this will simulate the request-response cycle)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 8080))
        client_socket.sendall(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
        
        response = client_socket.recv(1024).decode('utf-8')
        
        # Checks if the response contains the correct status code
        assert "HTTP/1.1 200 OK" in response
        assert "<h1>Welcome to the Home Page!</h1>" in response
        assert "Content-Length:" in response
        
        # Gets the content length from the response header
        content_length = int(response.split("Content-Length: ")[1].split("\r\n")[0])
        assert content_length == len("<html><body><h1>Welcome to the Home Page!</h1></body></html>")

def test_about_page():
    # Prepares a mock client connection (this will simulate the request-response cycle)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 8080))
        client_socket.sendall(b"GET /about HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
        
        response = client_socket.recv(1024).decode('utf-8')
        
        # Checks if the response contains the correct status code
        assert "HTTP/1.1 200 OK" in response
        assert "<h1>About Us</h1>" in response
        assert "We are a simple HTTP server." in response
        assert "Content-Length:" in response
        
        # Gets the content length from the response header
        content_length = int(response.split("Content-Length: ")[1].split("\r\n")[0])
        assert content_length == len("<html><body><h1>About Us</h1><p>We are a simple HTTP server. Ignore us!</p></body></html>")

def test_404_error():
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
