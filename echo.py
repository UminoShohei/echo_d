import socket
import os

def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 8080))
    connection.listen(5)
    os.fork()
    while True:
        conn, address = connection.accept()
        pid = os.fork()
        while True:
            data = conn.recv(2048)
            if data == ('close\r\n').encode('utf-8'):
                break
            elif data:
                conn.send(data)
                print(data)
        conn.shutdown(1)
        conn.close()
        exit()
if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass