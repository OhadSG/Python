# Ex 4.4 - HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules

# TO DO: set constants
import socket
import os

IP = "0.0.0.0"
PORT = 80
SOCKET_TIMEOUT = 5
DEFAULT_URL = r"/index.html"
MAX_REQUEST_LENGTH = 10000

REDIRECTION_DICTIONARY = {
    r'where.txt': r'here.txt'
}

FORBIDDEN = ['secret.txt', 'dont read.txt']


def get_file_data(filename):
    """ Get data from file """
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            return file.read()
    return b""


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    base = os.path.dirname(__file__)
    if resource == '/':
        url = base + DEFAULT_URL
    else:
        url = base + resource

    http_header = 'HTTP/1.0 '

    filename = url.split('/')[-1]
    filetype = filename.split('.')[-1]

    if filename in REDIRECTION_DICTIONARY:
        http_header += '302 Moved Temporarily\r\nLocation: ' + REDIRECTION_DICTIONARY[filename] + '\r\n'
    elif filename in FORBIDDEN:
        http_header += '403 Forbidden\r\n'
    elif not os.path.exists(url):
        http_header += '404 Not Found\r\n'
    else:
        http_header += '200 OK\r\n'

    if filetype == 'html' or filetype == 'txt':
        http_header += 'Content-Type: text/html; charset=utf-8\r\n'
    elif filetype == 'jpg':
        http_header += 'Content-Type: image/jpeg\r\n'
    elif filetype == 'js':
        http_header += 'Content-Type: text/javascript; charset=UTF-8\r\n'
    elif filetype == 'css':
        http_header += 'Content-Type: text/css\r\n'

    data = get_file_data(url) if http_header.startswith('HTTP/1.0 200 OK') else b""
    http_header += 'Content-Length: ' + str(len(data)) + '\r\n\r\n'

    http_response = http_header.encode() + data
    client_socket.send(http_response)


def validate_http_request(request):
    """ Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL """
    request = request.split('\r\n')[0]

    get = 'GET '
    get_len = len(get)
    version = ' HTTP/1.1'
    ver_len = len(version)

    if len(request) > (get_len + ver_len):
        if request[:get_len] == get and request[-ver_len:] == version:
            return True, request[get_len:-ver_len]
    return False, ""


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    while True:
        client_request = client_socket.recv(MAX_REQUEST_LENGTH).decode()
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')
            break
    print('Closing connection')
    client_socket.close()


def main():
    server_socket = socket.socket()
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print('New connection received')
            client_socket.settimeout(SOCKET_TIMEOUT)
            handle_client(client_socket)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
