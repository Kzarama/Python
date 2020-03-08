"""
Authors: Cristhian Castillo and Kevin Zarama
Icesi University, 2019
This script represent a Server in the model Client-Server for a Socket Chatroom
"""

import socket

# The select module gives us OS-level monitoring operations for things, including for sockets. It is especially useful in cases where
# we're attempting to monitor many connections simultaneously
import select

"""
HEADER DATA
"""
HEADER_LENGTH = 10

"""
HOST INFO
"""
HOST = "127.0.0.1"
PORT = 8080


# CREATE A SOCKET
# AF_INET address family, where host is a string representing either a hostname in Internet domain notation and port is a integer
# socket.SOCK_STREAM - TCP, conection-based.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the value of the given socket option
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the server informs operating system going to use a IP and Port
server_socket.bind((HOST, PORT))

# Listen new connections
server_socket.listen()

# List of sockets
sockets_list = [server_socket]

# List of connected clients. Is a dictionary with key (Socket) and user heder as data
clients = {}


print(f'Escuchando conexiones en {HOST}:{PORT}...')

def receive_message(client_socket):
    """ Manage received messages """
    try:
        # Receive the header that contain the length
        message_header = client_socket.recv(HEADER_LENGTH)

        # If don't recive data, the client close connection
        if not len(message_header):
            return False
        # Convert header to int
        message_length = int(message_header.decode('utf-8').strip())

        # Return an object of message header and message data
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return  False

while True:
    """
    The server wait and get notified
    """
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    # iterate Notifications
    for notified_socket in read_sockets:
        # If notified socket is a server socket - new connection, accept it
        if notified_socket == server_socket:
            # Accept the connection
            # Get the client socket
            # get the IP and port.
            client_socket, client_address = server_socket.accept()

            # Get the nick name of the user
            user = receive_message(client_socket)

            # If false, the client is disconnect
            if user is False:
                continue

            # Add the accepted Socket in sockets list
            sockets_list.append(client_socket)

            # Save the nickname of the user
            clients[client_socket] = user
            print('Nueva conexión de {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        else:
            # Receive the message
            message = receive_message(notified_socket)
            if message is False:
                print('Conexión Cerrada dede: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            # Get user by notified socket, so we will know who sent the message
            user = clients[notified_socket]

            print(f'Mensaje recibido de: {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]