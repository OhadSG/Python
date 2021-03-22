"""EX 2.6 protocol implementation
   Author: Ohad Solomon Gleicher
   Date: 14.11.2020
"""

import socket
import random
import time

LENGTH_FIELD_SIZE = 2
PORT = 8820

commands = {"RAND": lambda: str(random.randint(0, 10)),
            "NAME": lambda: "Bob the knob",
            "TIME": lambda: time.ctime(),
            "EXIT": lambda: ""}


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    if data in commands:
        return True
    return False


def create_msg(data):
    """Create a valid protocol message, with length field"""
    return str(len(data)).zfill(LENGTH_FIELD_SIZE) + data


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    if (msg_len := my_socket.recv(LENGTH_FIELD_SIZE).decode()).isdigit():
        return True, my_socket.recv(int(msg_len)).decode()
    return False, "Error"


def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    return commands[cmd]()
