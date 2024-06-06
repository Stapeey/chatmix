import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.184", 5050))

def handle_client(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(64).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            if msg == "!DISCONNECT":
                print(f"{addr} dc-d!")
                conn.close()
                connected = False
            print(f"{addr}: {msg}")
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"{addr} has joined!")
        print(f"{threading.active_count()-1} sockets are established.")
    return "server stopped."

print("starting server...")
print("running on 192.168.0.184:5050")
start()