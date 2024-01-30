import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"{username} has disconnected.")
                break
            print(f"{username}: {message}")
        except Exception as e:
            print(f"Error: {e}")
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(5)
    print("Server listening on port 5555...")

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")

        username = client.recv(1024).decode('utf-8')
        print(f"{username} has joined the chat.")

        client.send("Welcome to the chat!".encode('utf-8'))

        client_handler = threading.Thread(target=handle_client, args=(client, username))
        client_handler.start()

if __name__ == "__main__":
    start_server()
