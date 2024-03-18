import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).docode('utf-8')
            if not message:
                break
            print(f"Received message from {address}: {message}")
        except ConnectionResetError:
            break

    print(f"Connection with {address} closed.")
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Server listening on port 5555")


    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler()


if  __name__ == "__main__":
    start_server()


