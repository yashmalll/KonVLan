import socket

HOST = '0.0.0.0'
PORT = 5000
#создание TCP сокета
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#привязывание к ардесу и порту
server.bind((HOST, PORT))
#Переводит сокет в режим ожидания
server.listen()

print(f"Сервер запущен на порту {PORT}")

while True:
    #ожидание клиента и возвращение соедение и адреса
    conn, addr = server.accept()
    print(f"Подключился клиент: {addr}")

    conn.close()
