# Name : Vipin Saini
# Roll No : 24IMAI007
# Subject :Internet of Things

# Q2
# Part 1: TCP server
# Multi-Client TCP Chat Server


import socket
import threading

# Server configuration
HOST = '127.0.0.1'   # Localhost (change if needed)
PORT = 5000          # Port number

# List to keep track of connected clients
clients = []

def broadcast(message, sender_socket):
    """
    Send message to all connected clients
    except the sender.
    """
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                # If sending fails, remove client
                clients.remove(client)

def handle_client(client_socket, address):
    """
    Handle communication with a single client.
    This function runs in a separate thread.
    """
    print(f"[NEW CONNECTION] {address} connected.")
    
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            
            if not message:
                break  # Client disconnected
            
            print(f"[MESSAGE FROM {address}] {message.decode()}")
            
            # Broadcast message to other clients
            broadcast(message, client_socket)
        
        except:
            break

    # If client disconnects
    print(f"[DISCONNECTED] {address} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    """
    Start the TCP server and listen for connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        # Accept new client connection
        client_socket, address = server.accept()
        
        clients.append(client_socket)

        # Create a new thread for each client
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address)
        )
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()




