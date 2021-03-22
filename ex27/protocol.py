#   Ex. 2.7
#   Author: Ohad Solomon Gleicher
#   dec 2020

LENGTH_FIELD_SIZE = 4
PORT = 8820

commands = {
    'DIR': 1,
    'DELETE': 1,
    'COPY': 2,
    'EXECUTE': 1,
    'TAKE_SCREENSHOT': 0,
    'SEND_PHOTO': 0,
    'EXIT': 0
}


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """
    args = data.split()
    command = args[0]
    return command in commands and commands[command] == len(args) - 1


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    data = data.encode()
    data_len = str(len(data)).zfill(LENGTH_FIELD_SIZE)
    return data_len.encode() + data


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """

    len_field = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    if len_field.isdigit():
        msg = my_socket.recv(int(len_field)).decode()
        return True, msg
    return False, 'Error'
