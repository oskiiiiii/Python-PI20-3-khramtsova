import socket

sock = socket.socket()
msg = ''
print('Запуск сервера...')
try:
    sock.bind(('', 8080))
    print('Успешно')
    sock.listen()
    conn, addr = sock.accept()
    print('Клиент подключен')
    print('Адрес клиента: ' + str(addr))
    while msg != "exit":
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        conn.send(data)
        print('Сообщение: ' + str(msg))
except:
    print('Ошибка при запуске сервера')
