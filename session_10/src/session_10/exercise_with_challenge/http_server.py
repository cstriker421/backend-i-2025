import socket
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

HOST, PORT = '127.0.0.1', 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    logging.info(f"Serving HTTP on {HOST} port {PORT} ...")

    while True:

        client_connection, client_address = server_socket.accept()
        with client_connection:

            request_data = client_connection.recv(1024).decode('utf-8')
            logging.info(f"Received request from {client_address}:")
            logging.debug(request_data)

            lines = request_data.splitlines()
            if lines:
                request_line = lines[0]
                method, path, _ = request_line.split()
                logging.info(f"Method: {method}, Path: {path}")

                if path == '/':
                    body = "<html><body><h1>Welcome to the Home Page!</h1></body></html>"
                    status_code = "200 OK"
                elif path == '/about':
                    body = "<html><body><h1>About Us</h1><p>We are a simple HTTP server. Ignore us!</p></body></html>"
                    status_code = "200 OK"
                else:
                    body = "<html><body><h1>404 Error</h1><p>Nothing here but grues!</p></body></html>"
                    status_code = "404 Not Found"

                content_length = len(body) # Content length calculated by body length to facilitate code

                http_response = (
                    f"HTTP/1.1 {status_code}\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    f"Content-Length: {content_length}\r\n"
                    "\r\n"
                    f"{body}"
                )

            client_connection.sendall(http_response.encode('utf-8'))
            logging.info(f"Sent response for {path}")
