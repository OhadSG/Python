"""EX 2.6 client implementation
   Author: Ohad Solomon Gleicher
   Date: 14.11.2020
"""

import socket
import protocol


def main():
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", protocol.PORT))

    while True:
        user_input = input("Enter command:\n")
        valid_cmd = protocol.check_cmd(user_input)  # check if the entered command is valid

        if valid_cmd:
            msg = protocol.create_msg(user_input)  # create a formatted msg to be send to the server
            my_socket.send(msg.encode())
            if user_input == "EXIT":
                break
            valid, msg = protocol.get_msg(my_socket)  # check the response and returns it's text
            if valid:
                print(msg)
            else:
                print("Response not valid\n")
        else:
            print("Not a valid command")

    print("Closing\n")
    my_socket.close()


if __name__ == "__main__":
    main()
