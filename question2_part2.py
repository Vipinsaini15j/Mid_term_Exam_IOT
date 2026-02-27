# Name Vipin Saini
# Roll No :24IMAI007
# Subject Internet of Things

# Question 2:
# Part2 TCP Client 

# Multi-Client TCP Chat Client


import socket
import threading

HOST = '127.0.0.1'   # Same as server
PORT = 5000

def receive_messages(client_socket):
    """
    Continuously receive broadcast messages
    from the server.
    Runs in a separate thread.
    """
    while True:
        try:
            message = client_socket.recv(1024)
            print("\n" + message.decode())
        except:
            print("Disconnected from server.")
            client_socket.close()
            break

def send_messages(client_socket):
    """
    Continuously send user input to server.
    """
    while True:
        message = input()
        client_socket.send(message.encode())

def start_client():
    """
    Connect to the server and start
    send/receive threads.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
    client.connect((HOST, PORT))

    print("Connected to chat server.")

    # Thread for receiving messages
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,)
    )
    receive_thread.start()

    # Thread for sending messages
    send_thread = threading.Thread(
        target=send_messages,
        args=(client,)
    )
    send_thread.start()

if __name__ == "__main__":
    start_client()

# ------------------------------------------------------------------------------------------------