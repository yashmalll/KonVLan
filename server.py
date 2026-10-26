import socket

HOST = '0.0.0.0'

PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Сервер запущен на порту {PORT}")
while True:
    conn, addr = server.accept()
    print(f"Подключился клиент: {addr}")

    data = conn.recv(1024)
    print("Сообщение:", data.decode("utf-8"))

    conn.sendall("Сообщение получено!".encode("utf-8"))

    conn.close()
