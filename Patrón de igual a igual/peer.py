import socket
import threading

HOST = 'localhost'
PORT = 5000

def handle_client(client_socket):
    """ Maneja la comunicación con el cliente. """
    while True:
        msg = client_socket.recv(1024).decode('utf-8')
        if not msg:
            break
        print(f"Mensaje recibido: {msg}")
        response = "Mensaje recibido"
        client_socket.send(response.encode('utf-8'))
    client_socket.close()

def start_server():
    """ Inicia el servidor y acepta conexiones entrantes. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexión establecida con {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def start_client(message):
    """ Inicia el cliente que se conecta al servidor y envía un mensaje. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(message.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {response}")
    client.close()

if __name__ == "__main__":
    choice = input("Elige 'servidor' para iniciar como servidor o 'cliente' para iniciar como cliente: ")
    if choice == 'servidor':
        start_server()
    elif choice == 'cliente':
        msg = input("Ingresa el mensaje para enviar al servidor: ")
        start_client(msg)
    else:
        print("Opción no válida")
