import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.184", 5050))

def send(msg):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b' ' * (64-len(send_length))
    client.send(send_length)
    client.send(message)

dc = False
a = ""
while a != "!!!":
    a = input()
    if a == "!DISCONNECT":
        dc = True
    if dc:
        if a == "reconnect":
            dc = False
            client.connect(("192.168.0.184", 5050))
        else:
            pass
    else:
        send(a)