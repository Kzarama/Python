"""
Authors: Cristhian Castillo and Kevin Zarama
Icesi University, 2019
This script represent a client in the model Client-Server for a Socket Chatroom
"""

import socket
import sys
import errno
from random import randrange

"""
HEADER INFO
"""

HEADER_LENGTH = 10

"""
HOST INFO
"""
HOST = "127.0.0.1"
PORT = 8080
nickname = input("Username: ")

"""
CIPHER DATA
"""
# Key for cesar cipher
key = randrange(20) + 1
hex_key = hex(key)

# Alphabet for Cesar Cipher
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz"


def encoded_message(msg):
    """
    Encode a message using Cesar Cipher
    :param msg: Is the message to Cipher
    :return: The encrypted Message
    """
    encoded_msg = ""

    for letter in msg:
        if letter in abc:
            index = abc.index(letter)
            aux = index + key
            if aux >= len(abc):
                encoded_msg += abc[key - (len(abc) - index)]
            else:
                encoded_msg += abc[aux]
        else:
            encoded_msg += letter
    return encoded_msg


def decoded_message(msg, cesar_key):
    """
    Decoded the encrypted message
    :param msg: encrypted message for decoded
    :param cesar_key: number of movements
    :return: Messaged decoded
    """
    message = ""
    for letter in msg:
        index = abc.index(letter)
        aux = index - cesar_key
        if aux < 0:
            message += abc[len(abc) + aux]
        else:
            message += abc[aux]
    return message


# Create a socket
# socket.SOCK_STREAM - TCP, conection-based.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port of the Host
client_socket.connect((HOST, PORT))

# Connection to non-blocking state
client_socket.setblocking(False)

"""
User Information. And Encode header in bytes using utf-8
"""
username = nickname.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    # Wait for user to input a message
    message = input(f'{nickname} > ')
    encrypted_message = encoded_message(message)

    # If message is not empty - send it
    if encrypted_message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        encrypted_message = encrypted_message.encode('utf-8') + hex_key.encode('utf-8')
        message_header = f"{len(encrypted_message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + encrypted_message)

    try:
        # Loop over received messages and print them
        while True:

            # Receive header containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection.
            if not len(username_header):
                print('Conexión cerrada por el servidor :(')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any
            # length)
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            encrypted_message = client_socket.recv(message_length).decode('utf-8')

            # Get the key for cesar cipher and the message encoded
            key_index = encrypted_message.index("0x")
            msg = encrypted_message[0:key_index]
            cesar_key = int(encrypted_message[key_index:], 0)

            # decode the message
            msg = decoded_message(msg, cesar_key)
            # Print message
            print(f'{username} > {msg}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # Check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Error de lectura: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Error de lectura: '.format(str(e)))
        sys.exit()
