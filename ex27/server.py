#   Ex. 2.7
#   Author: Ohad Solomon Gleicher
#   dec 2020
import glob
import shutil
import socket
import subprocess

import pyautogui

import protocol
import os

IP = "0.0.0.0"
PHOTO_PATH = r'C:\Users\User\Pictures\serverSS.jpg'  # The path + filename where the screenshot at the server should be saved


def DIR(path):
    return '\n'.join(glob.glob(path + r'\*.*')).replace(path + '\\', "")


def DELETE(path):
    os.remove(path)


# I always wondered if you actually check the code, here's a funny meme in case you do
# https://miro.medium.com/max/1274/1*ON_d7DWgW8g8uu3EBntfNw.png

def COPY(file, copy_to):
    path = shutil.copy(file, copy_to)
    return "File copied!" if path == copy_to else "Copy failed successfully"


def EXECUTE(path):
    return "Program executed successfully" if subprocess.call(path) == 0 else "Program failed successfully"


def TAKE_SCREENSHOT():
    pyautogui.screenshot().save(PHOTO_PATH)


def SEND_PHOTO():
    with open(PHOTO_PATH, 'rb') as file:
        return file.read()


commands = {
    'DIR': DIR,
    'DELETE': DELETE,
    'COPY': COPY,
    'EXECUTE': EXECUTE,
    'TAKE_SCREENSHOT': TAKE_SCREENSHOT,
    'SEND_PHOTO': SEND_PHOTO,
    'EXIT': lambda: None
}


def check_client_request(cmd):
    """
    Break cmd to command and parameters
    Check if the command and params are good.

    For example, the filename to be copied actually exists

    Returns:
        valid: True/False
        command: The requested cmd (ex. "DIR")
        params: List of the cmd params (ex. ["c:\\cyber"])
    """
    # Use protocol.check_cmd first
    if protocol.check_cmd(cmd):
        # Then make sure the params are valid
        s = cmd.split()
        cmd = s[0]
        params = s[1:]
        for param in params:
            if not os.path.exists(param):
                return False, "Error", []
        return True, cmd, params

    # (6)
    return False, "Error", []


def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_PHOTO, only the length of the file will be sent

    Returns:
        response: the requested data

    """

    # (7)

    num_of_args = len(params)
    if num_of_args == 0:
        response = commands[command]()
    elif num_of_args == 1:
        response = commands[command](params[0])
    else:
        response = commands[command](params[0], params[1])

    response = "" if response is None else response
    if command == "SEND_PHOTO":
        return str(len(response))

    return response


def main():
    # open socket with client
    server_socket = socket.socket()
    server_socket.bind((IP, protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    # (1)

    # handle requests until user asks to exit
    while True:
        # Check if protocol is OK, e.g. length field OK

        valid_protocol, cmd = protocol.get_msg(client_socket)
        if valid_protocol:
            # Check if params are good, e.g. correct number of params, file name exists
            valid_cmd, command, params = check_client_request(cmd)
            if valid_cmd:

                # (6)

                # prepare a response using "handle_client_request"
                response = handle_client_request(command, params)
                # add length field using "create_msg"
                response = protocol.create_msg(response)

                # send to client
                client_socket.send(response)
                if command == 'SEND_PHOTO':
                    # Send the data itself to the client
                    client_socket.send(commands["SEND_PHOTO"]())
                    # (9)

                if command == 'EXIT':
                    break
            else:
                # prepare proper error to client
                response = 'Bad command or parameters'
                # send to client
                client_socket.send(protocol.create_msg(response))

        else:
            # prepare proper error to client
            response = 'Packet not according to protocol'
            # send to client
            client_socket.send(protocol.create_msg(response))

            # Attempt to clean garbage from socket
            client_socket.recv(1024)

    # close sockets
    print("Closing connection")


if __name__ == '__main__':
    main()
